import random
import math
import time
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def calc_fitness(min_order, min_distance, locations, population, fitness):
   fitness.clear()

   for p in population:
      length = len(p) - 1

      total = 0
      for i in range(length):
         total += ssd.euclidean(locations[p[i]], locations[p[i+1]])

      if total < min_distance[0]:
         min_distance[0] = total
         min_order.clear()
         min_order.extend(p)

      fitness.append(1 / (math.pow(total, 8) + 1) )

   return

def normalize_fitness(fitness):
   summation = 0
   for val in fitness:
      summation += val

   for i in range(len(fitness)):
      fitness[i] = fitness[i] / summation

   return
      
def evolve(population, fitness):
   mutation_rate = 0.01
   new_gen = list()

   for i in range(len(population)):
      order_1 = choose(population, fitness)
      order_2 = choose(population, fitness)

      order = crossover(order_1, order_2)
      mutate(order, mutation_rate)
      new_gen.append(order)

   population.clear()
   population.extend(new_gen)

   return

def crossover(order_1, order_2):
   length = len(order_1) - 1
   start = math.floor(random.randint(0, length))
   end = math.floor(random.randint(start + 1, length+1))

   order = order_1[start : end]

   for val in order_2:
      if val not in order:
         order.append(val)

   return order

def mutate(order, mutation_rate):
   length = len(order)

   for l in range(length):
      if random.random() < mutation_rate:
         i = math.floor(random.randint(0, length-1))
         j = (i + 1) % length
         
         temp = order[i]
         order[i] = order[j]
         order[j] = temp

   return

def choose(population, fitness):
   index = 0
   rate = random.random()

   while rate > 0:
      rate -= fitness[index]
      index += 1

   index -= 1

   if index > len(population):
      index = len(population) - 1

   return population[index].copy()

def create_population(num_points, pop_size):
   adam = [i for i in range(num_points)]
   population = list()

   for i in range(pop_size):
      population.append(adam)
      random.shuffle(adam)

   return population

def life(min_order, min_distance, population, locations, fitness):
   calc_fitness(min_order, min_distance, locations, population, fitness)

   normalize_fitness(fitness)

   evolve(population, fitness)
   
   return min_distance, min_order

def show_plot(num_points, locations, to_plot):
   pop_size = num_points * 3
   min_distance = [math.inf]
   min_order = list()
   fitness = list()
   num_generations = 1

   population = create_population(num_points,  pop_size)

   genetic_start = time.time()
   while num_generations < 100:
      min_distance, min_order = life(min_order, min_distance, population, locations, fitness)
      num_generations += 1

   genetic_end = time.time()
   t = genetic_end - genetic_start

   if to_plot:
      fig = plt.figure('Genetic Algorithm')
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
      
      plt.savefig('genetic_algorithm_graph.png')

   # args = (min_order, min_distance, population, locations, fitness)
   # animate = animation.FuncAnimation(fig, update, fargs=args)
   # plt.show()

   return min_distance, min_order, t
