import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import math
import scipy.spatial.distance as ssd
import time

# splits location array into x and y coordinates for graphing
def split(coordinates, order):
   x = list()
   y = list()

   for o in order:
      point = coordinates[o]
      x.append(point[0])
      y.append(point[1])

   return x, y

def swap(lexicographic_order, i, j):
   temp = lexicographic_order[i]
   lexicographic_order[i] = lexicographic_order[j]
   lexicographic_order[j] = temp
   return

def lexo_order(lexicographic_order):

   # find second largest number in array with given order
   largest_i = -1
   for i in range(len(lexicographic_order) - 1):
      if lexicographic_order[i] < lexicographic_order[i+1]:
         largest_i = i

   # if no number found, all permutations have been done
   if largest_i == -1:
      return 1
   
   # find index with number larger than number at index i
   largest_j = -1
   for j in range(len(lexicographic_order)):
      if lexicographic_order[largest_i] < lexicographic_order[j]:
         largest_j = j

   # swap two values
   swap(lexicographic_order, largest_i, largest_j)

   # reverse array from largest_i + 1 to end
   sliced = lexicographic_order[largest_i+1:]

   # store order beginning of order
   keep = lexicographic_order[0: largest_i + 1]

   # reverse sliced and add back to keep list
   sliced.reverse()
   keep.extend(sliced)
   
   # clear lexicographic list for new order
   lexicographic_order.clear()
   lexicographic_order.extend(keep)

   return 0

def no_plot(location, lexicographic_order, min_distance, min_order):
   # calculate distance
   total_distance = 0
   for i, index in enumerate(lexicographic_order):
      if i == len(lexicographic_order) - 1:
         break

      total_distance += ssd.euclidean(location[index], location[lexicographic_order[i+1]])

   # store shortest distance and location sequence
   if total_distance < min_distance[0]:
      min_distance[0] = total_distance
      min_order.clear()
      min_order.extend(lexicographic_order)

   # update order
   end = lexo_order(lexicographic_order)

   return min_distance, min_order, end

def update(frame, location, ax1, ax2, lexicographic_order, min_distance, min_order):
   # split locations into x andy coordinates for graphing
   x, y = split(location, lexicographic_order)

   # calculate distance
   total_distance = 0
   for i, index in enumerate(lexicographic_order):
      if i == len(lexicographic_order) - 1:
         break

      total_distance += ssd.euclidean(location[index], location[lexicographic_order[i+1]])
   
   # store shortest distance and location sequence
   if total_distance < min_distance[0]:
      min_distance[0] = total_distance
      min_order.clear()
      min_order.extend(lexicographic_order)

   best_x, best_y = split(location, min_order)

   # plot locations
   # clear previous graphs
   ax1.clear()
   ax2.clear()

   # make titles the order being shown
   ax1.title.set_text(str(min_order))
   ax2.title.set_text(str(lexicographic_order))

   # add index labels to points
   for i in range(len(min_order)):
      ax1.annotate(str(i), (location[i][0], location[i][1]))
      ax2.annotate(str(i), (location[i][0], location[i][1]))

   ax1.plot(best_x, best_y, marker='.', markersize=12.0, color='red')
   ax2.plot(x, y, marker='.', markersize=12.0)

   # update order
   end = lexo_order(lexicographic_order)

   return min_distance, min_order, end

def animate_search():
   # plot variables
   fig = plt.figure('Lexicographi Order: Brute Force')
   fig.subplots_adjust(hspace=0.5)
   ax1 = fig.add_subplot(2, 1, 1)
   ax2 = fig.add_subplot(2, 1, 2)

   # start plot
   args = (location, ax1, ax2, lexicographic_order, min_distance, min_order)
   animate = animation.FuncAnimation(fig, update, fargs=args)
   plt.show()

   return

def show_plot(locations, num_points, to_plot):
   min_distance = [math.inf]
   min_order = list()
   lexicographic_order = [i for i in range(num_points)]

   # find way to calc distances efficiently

   brute_start = time.time()
   end = 0
   while end != 1:
      min_distance, min_order, end = no_plot(locations, lexicographic_order, min_distance, min_order)

   brute_end = time.time()
   t = brute_end - brute_start

   if to_plot:
      fig = plt.figure('Lexicographi Order: Brute Force')
      ax = fig.add_subplot(1, 1, 1)

      # set title of graph to order being shown
      ax.title.set_text(str(min_order))

      # add index labels to points
      x = list()
      y = list()
      for i in range(len(min_order)):
         ax.annotate(str(i), (locations[i][0], locations[i][1]))
         x.append(locations[i][0])
         y.append(locations[i][1])

      ax.plot(x, y, marker='.', markersize=12.0)

      plt.savefig('lexicographic_order_graph.png')

   return min_distance, min_order, t