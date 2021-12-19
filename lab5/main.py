from random import randint, uniform

import numpy as np
from matplotlib import pyplot as plt

from factory import Factory
from city import City
import genetic as ga

#            Города
#     A    B   C   D   E   F    Заводы
G = ((1,  10,  2,  4,  3,  2),  # A
     (10,  1,  6, 15,  1,  5),  # B
     (2,   6,  6,  3,  9,  1),  # C
     (4,  15,  3,  6,  5,  6))  # D

MUTATION_POSSIBILITY = 0.25
NUM_OF_GENERATIONS = 30
NUM_OF_POPULATION = 6
PRODUCTION_SUPPORT_VALUE = randint(20, 70)

NUM_OF_FACTORIES = len(G)
NUM_OF_CITIES = len(G[0])
NUM_OF_PARENTS = int(NUM_OF_POPULATION / 2)


def generate_cities():
    cities = []
    for j in range(NUM_OF_CITIES):
        lower_bound = PRODUCTION_SUPPORT_VALUE / NUM_OF_CITIES * 0.75
        higher_bound = PRODUCTION_SUPPORT_VALUE / NUM_OF_CITIES * 1.25
        cities.append(City(uniform(lower_bound, higher_bound), j))

    return cities


def generate_factories():
    factories = []
    for j in range(NUM_OF_FACTORIES):
        lower_bound = PRODUCTION_SUPPORT_VALUE / NUM_OF_FACTORIES * 0.75
        higher_bound = PRODUCTION_SUPPORT_VALUE / NUM_OF_FACTORIES * 1.25
        factories.append(Factory(uniform(lower_bound, higher_bound), j))

    return factories


cities = generate_cities()
factories = generate_factories()
population = ga.generate_pop(NUM_OF_POPULATION, NUM_OF_FACTORIES, NUM_OF_CITIES, factories)

mean_fitnesses = []
min_fitnesses = []
for i in range(NUM_OF_GENERATIONS):
    fitness = ga.cal_pop_fitness(population, cities, factories, G)
    parents = ga.select_mating_pool(population, fitness, NUM_OF_PARENTS)
    childs = ga.mutation(MUTATION_POSSIBILITY, ga.crossover(parents))
    population = ga.sort_population(population, fitness, NUM_OF_PARENTS, childs)
    min_fitnesses.append(np.min(fitness))

plt.plot(min_fitnesses)
plt.xlabel('Поколение')
plt.ylabel('Минимальная приспособленность')
plt.title('График минимальных значений приспособленности')
plt.show()
