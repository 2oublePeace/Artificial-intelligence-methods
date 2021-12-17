import math

import genetic as ga

inf = 900

#     A     B     C    D
G = ((0,   10,    2,   4),  #A
     (10,   0,   inf,  15), #B
     (2,   inf,   0,   3),  #C
     (4,   15,    3,   0))  #D

production_consumption = [20, 20, 5, 5]
node_type = ['factory', 'factory', 'city', 'city']

num_nodes = len(G)
num_chrom = math.factorial(num_nodes - 1)
num_parents_mating  = 2
pop_size = (num_chrom, num_nodes)

new_population = ga.generate_pop(num_chrom, num_nodes, 0)
fitness = ga.cal_pop_fitness(production_consumption, new_population, G, node_type)
parents = ga.select_mating_pool(new_population, fitness, num_parents_mating)


crossover = ga.crossover(parents, (parents.shape[0], num_nodes))
print(crossover)




