import math
from random import randint, uniform
from factory import Factory
from city import City
import numpy as np
import genetic as ga

#     A     B     C    D
G = ((1, 10, 2, 4, 3, 2),  # A
     (10, 1, 6, 15, 1, 5),  # B
     (2, 6, 6, 3, 9, 1),  # C
     (4, 15, 3, 6, 5, 6))  # D

mutation_possibility = 0.15
NUM_OF_FACTORIES = 4
NUM_OF_CITIES = 6
NUM_OF_GENERATIONS = 5
NUM_OF_POPULATION = 5
PRODUCTION_SUPPORT_VALUE = randint(20, 70)


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


def generate_chromosomes(factories):
    population = []
    for i in range(NUM_OF_POPULATION):
        chromosome = []
        for j in range(NUM_OF_FACTORIES):
            genes = []
            for k in range(NUM_OF_CITIES):
                genes.append(factories[j].production / NUM_OF_CITIES * (1 + 0.15 * randint(-1,1)))
            chromosome.append(genes)
        population.append(chromosome)

    return population


def fitness(population, factories, cities):
    fitness = np.empty((len(population[0])))

    for i in range(len(population)):
        chromosomes = population[i]
        for j in range(len(chromosomes)):
            remains = 0
            genes = chromosomes[j]
            for k in range(len(genes)):
                fitness[j] += genes[k] * G[j][k]
                remains += genes[k]

                if remains > cities[k].consumption * 1.1:
                    fitness[j] += 500
            if remains > factories[j].production:
                    fitness[j] += 500


    return fitness


cities = generate_cities()
factories = generate_factories()
population = generate_chromosomes(factories)
fitness(population, factories, cities)
