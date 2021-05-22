import random
import time
import dijkstra
import lexicographic_order
import genetic_algorithm

def get_points(num_points):
   locations = list()

   for i in range(num_points):
      l = [random.random() * 10, random.random() * 10]
      locations.append(l)

   return locations

def dijkstra_method(num_points, locations, to_plot):
   dijkstra_start = time.time()

   graph = dijkstra.Graph
   dijkstra.fill_graph(graph, locations)
   graph.add_edges(graph)
   graph.calc_distance(graph)

   routes = dijkstra.dijkstra(graph)
   graph.print_graph(graph)

   dijkstra_end = time.time()
   dijkstra_time = dijkstra_end - dijkstra_start

   print('time taken = ' + str(dijkstra_time) + ' seconds')
   print('dijkstra value')
   min_order, min_distance = dijkstra.print_dictionary(routes, num_points)
   print()

   if to_plot:
      dijkstra.plot_graph(locations, min_order)

   del(graph)

   return

def genetics(num_points, locations, to_plot):
   genetic_distance, genetic_order, genetic_time = genetic_algorithm.show_plot(num_points, locations, to_plot)
   print('time taken = ' + str(genetic_time) + ' seconds')
   print('genetic algorithm')
   print(genetic_order, genetic_distance)
   print()

   return

def brute_force(num_points, locations, to_plot):
   brute_distance, brute_order, brute_time = lexicographic_order.show_plot(locations, num_points, to_plot)
   print('time taken = ' + str(brute_time) + ' seconds')
   print('brute force algorithm')
   print(brute_order, brute_distance)
   print()

   return

def main():

   # to_plot is either 1 or 0
   # 1 to show plot of best path
   to_plot = 1

   # get location data
   num_points = 5
   locations = get_points(num_points)

   # dijkstra method implementation
   dijkstra_method(num_points, locations, to_plot)

   # genetic algorithm
   genetics(num_points, locations, to_plot)

   # brute force method implementation
   brute_force(num_points, locations, to_plot)

   print()

   return

if __name__ == '__main__':
   main()