import numpy as np
import math


def generate_pop(num_chrom, num_nodes, start_node):
    if num_chrom > math.factorial(num_nodes - 1):
        pop = np.zeros((math.factorial(num_nodes - 1), num_nodes))
    else:
        pop = np.zeros((num_chrom, num_nodes))

    new_chrom = np.arange(num_nodes)
    for i in range(pop.shape[0]):
        np.random.shuffle(new_chrom)
        if new_chrom[0] != start_node:
            start_index = np.where(new_chrom == start_node)
            temp = new_chrom[0]
            new_chrom[0] = new_chrom[start_index]
            new_chrom[start_index] = temp

        while new_chrom.tolist() in pop.tolist():
            np.random.shuffle(new_chrom)
            if new_chrom[0] != start_node:
                start_index = np.where(new_chrom == start_node)
                temp = new_chrom[0]
                new_chrom[0] = new_chrom[start_index]
                new_chrom[start_index] = temp

        pop[i] = new_chrom

    return pop


def cal_pop_fitness(production_consumption, pop, G, node_type):
    fitness = np.empty(pop.shape[0])
    for i in range(pop.shape[0]):
        road_length = 0
        remains = 0
        cities_count = 0
        for k in range(pop.shape[1]):
            if node_type[int(pop[i][k])] == 'city':
                cities_count += 1
        for j in range(pop.shape[1]):
            if j < pop.shape[1] - 1:
                road_length += G[int(pop[i][j])][int(pop[i][j + 1])]
            if node_type[int(pop[i][j])] == 'factory' and cities_count > 0:
                remains = remains + production_consumption[int(pop[i][j])]
            elif remains > production_consumption[int(pop[i][j])] + production_consumption[int(pop[i][j])] * 0.1:
                remains -= production_consumption[int(pop[i][j])]
                cities_count -= 1
            else:
                cities_count -= 1
        print(road_length, remains)
        fitness[i] = road_length + remains * 10

    return fitness


def select_mating_pool(pop, fitness, num_parents):
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_index = np.where(fitness == np.min(fitness))[0][0]
        parents[parent_num, :] = pop[max_fitness_index, :]
        fitness[max_fitness_index] = 99999999999

    return parents


def crossover(parents, offspring_size):
    offspring = np.zeros(offspring_size)
    crossover_point = np.uint8(offspring_size[1] / 2)

    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]

        unique_second_parent = np.setdiff1d(parents[parent2_idx, crossover_point:], offspring[k, 0:crossover_point])
        unique_union = np.union1d(offspring[k, 0:crossover_point], unique_second_parent)
        unique_remain = np.setdiff1d(parents[parent1_idx, :], unique_union)

        np.setdiff1d(parents[parent2_idx, crossover_point:], offspring[k, 0:crossover_point])
        offspring[k, crossover_point:] = np.union1d(unique_second_parent, unique_remain)

    return offspring
