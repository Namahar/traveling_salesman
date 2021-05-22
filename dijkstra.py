import random
import math
import matplotlib.pyplot as plt

class Vertex:
   def __init__(self, location):
      self.x = location[0]
      self.y = location[1]
      self.neighbors = list()
      self.distances = list()

      return

   def add_neighbors(self, key, length):
      for i in range(length):
            if i != key:
               self.neighbors.append(i)

      return

   def add_distance(self, vertices, neighbor):
      vertex = vertices[neighbor]
      x = (self.x - vertex.x)**2
      y = (self.y - vertex.y)**2
      d = (x + y)**0.5
      self.distances.append(d)

      return

class Graph:
   vertices = dict()
   num_vertices = 0

   def add_vertex(self, vertex):
      self.vertices[self.num_vertices] = vertex
      self.num_vertices += 1

      return

   def add_edges(self):
      for key, vertex in self.vertices.items():
         vertex.add_neighbors(key, self.num_vertices)

      return

   def calc_distance(self):
      for key, vertex in self.vertices.items():
         for neighbor in vertex.neighbors:
            vertex.add_distance(self.vertices, neighbor)

      return

   def print_graph(self):
      for key, val in self.vertices.items():
         print('key = ' + str(key))
         print('location = ' + str(val.x) + '\t' + str(val.y))
         print('neighbors = ' + str(val.neighbors))
         print('distances = ' + str(val.distances))
         print()

      return

def dijkstra(g):
   scores = dict()

   # use each node as a starting point
   for i in range(g.num_vertices):

      # get vertex object
      start_vertex = g.vertices[i]
      
      unvisited = [k for k in range(g.num_vertices)]
      visited = list()
      distance = 0

      visited.append(unvisited.pop(i))
      
      while len(unvisited) > 0:
         # check neighbors of vertex for shortest distance
         lowest_distance = math.inf
         next_neighbor = math.inf
         for j in range(len(start_vertex.neighbors)):
            if start_vertex.distances[j] < lowest_distance:
               if start_vertex.neighbors[j] in unvisited:
                  lowest_distance = start_vertex.distances[j]
                  next_neighbor = start_vertex.neighbors[j]

         distance += lowest_distance

         # go to next node
         index = unvisited.index(next_neighbor)
         v = unvisited.pop(index)
         visited.append(v)
         start_vertex = g.vertices[next_neighbor]

      visited.append(distance)
      scores[i] = visited

   return scores

def fill_graph(g, locations):
   for loc in locations:
      point = Vertex([loc[0], loc[1]])
      g.add_vertex(g, point)

def print_dictionary(routes, num_points):
   min_val = math.inf
   min_order = list()
   for key, val in routes.items():
      # print(val)
      if val[num_points] < min_val:
         min_val = val[num_points]
         min_order = val[0:num_points]

   # print()
   print(min_order, min_val)

   return min_order, min_val

def plot_graph(locations, min_order):
   fig = plt.figure('Dijkstra Algorithm')
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

   plt.savefig('dijkstra_algorithm_graph.png')
