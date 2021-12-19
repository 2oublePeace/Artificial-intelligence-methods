from random import randint
import numpy as np


def generate_pop(NUM_OF_POPULATION, NUM_OF_FACTORIES, NUM_OF_CITIES, factories):
    population = []
    for i in range(NUM_OF_POPULATION):
        chromosome = []
        for j in range(NUM_OF_FACTORIES):
            genes = []
            for k in range(NUM_OF_CITIES):
                genes.append(factories[j].production / NUM_OF_CITIES * (1 + 0.15 * randint(-1, 1)))
            chromosome.append(genes)
        population.append(chromosome)

    return population


def cal_pop_fitness(population, cities, factories, G):
    fitness = np.zeros((len(population)))

    for i in range(len(population)):
        chromosome = population[i]
        for j in range(len(chromosome)):
            gene = chromosome[j]
            for k in range(len(gene)):
                fitness[i] += gene[k] * G[j][k]
                if gene[k] > cities[k].consumption * 1.1:
                    fitness[i] += fitness[i] * (abs(gene[k] - cities[k].consumption * 1.1) / 10)
                if gene[k] > factories[j].production:
                    fitness[i] += 500

    return fitness


def select_mating_pool(pop, fitness, num_parents):
    min_fitness = np.copy(fitness)
    population = np.array(pop)
    parents = np.zeros((num_parents, population.shape[1], population.shape[2]))
    for parent_num in range(num_parents):
        min_fitness_index = np.where(min_fitness == np.min(min_fitness))[0][0]
        parents[parent_num] = pop[min_fitness_index]
        min_fitness[min_fitness_index] = 99999999999

    return parents


def crossover(parents):
    offspring = np.zeros(parents.shape)
    crossover_point = np.uint8(offspring.shape[1] / 2)

    for k in range(offspring.shape[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point, :] = parents[parent1_idx, 0:crossover_point, :]
        offspring[k, crossover_point:, :] = parents[parent2_idx, crossover_point:, :]

    return offspring


def mutation(mut_percent, childs):
    for i in range(childs.shape[0]):
        if randint(0, 100) < mut_percent * 100:
            child1_idx = randint(1, childs.shape[1]) - 1
            child2_idx = randint(1, childs.shape[1]) - 1

            while child1_idx == child2_idx:
                child2_idx = randint(1, childs.shape[1]) - 1

            swap_offspring = childs[i][child1_idx][:]
            childs[i][child1_idx][:] = childs[i][child2_idx][:]
            childs[i][child2_idx][:] = swap_offspring

    return childs


def sort_population(pop, fitness, num_of_parents, childs):
    population = np.array(pop)
    sorting_fitness = np.copy(fitness)
    sorted_indexes = np.zeros(fitness.shape)
    new_population = np.zeros((population.shape[0] - num_of_parents, population.shape[1], population.shape[2]))
    for i in range(sorting_fitness.shape[0]):
        sorted_indexes[i] = np.argmax(sorting_fitness)
        sorting_fitness = np.where(sorting_fitness == np.max(sorting_fitness), -99999999999, sorting_fitness)

    for i in range(new_population.shape[0]):
        index = sorted_indexes[i]
        new_population[i][:][:] = population[int(index)][:][:]

    return np.vstack((new_population, childs))
