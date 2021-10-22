import random
import numpy as np
import pandas

tableName = 'auto_stat.csv'
tables = ['C02 realease', '02 consuming', 'Horsepowers', 'Wheel size']


def createMatrix():
    co2_vector = np.random.random((500, 1))
    o2_vector = np.random.random((500, 1))
    hp_vector = np.random.randint(25, 400, (500, 1))
    wheelsize_vector = np.random.randint(13, 29, (500, 1))

    matrix = np.hstack([co2_vector, o2_vector, hp_vector, wheelsize_vector])
    matrix_frame = pandas.DataFrame(matrix, columns=tables)
    return matrix_frame


def make_noise(matrix):
    mu, sigma = 0, 0.5
    noise = np.random.normal(mu, sigma, size=500)
    matrix['C02 realease'] += noise
    matrix['02 consuming'] += noise
    matrix['Horsepowers'] += noise * avg(tableName, 2)
    matrix['Wheel size'] += noise * avg(tableName, 3)

    for i in range(len(matrix) // 4):
        random_row = random.randint(0, len(matrix) - 1)
        random_table = random.randint(0, len(tables) - 1)
        matrix[tables[random_table]].values[random_row] = None

    return matrix


def uploadCSV(matrix):
    matrix.to_csv('auto_stat.csv', sep=';', index=False)


def downloadCSV(tableName):
    matrix_frame = pandas.read_csv(tableName, delimiter=';')
    print(matrix_frame)


def avg(tableName, column_index):
    matrix_frame = pandas.read_csv(tableName, delimiter=';')
    date_frame = pandas.read_csv(tableName, delimiter=';')
    avg = matrix_frame[tables[column_index]].mean(skipna=True)
    print("Average value in table", avg, "\n")
    return avg


def median(tableName, column_index):
    matrix_frame = pandas.read_csv(tableName, delimiter=';')
    print("Median value in table", matrix_frame[[tables[column_index]]].median(skipna=True), "\n")


def min(tableName, column_index):
    matrix_frame = pandas.read_csv(tableName, delimiter=';')
    print("Min value in table", matrix_frame[[tables[column_index]]].min(skipna=True), "\n")


def max(tableName, column_index):
    matrix_frame = pandas.read_csv(tableName, delimiter=';')
    print("Max value in table", matrix_frame[[tables[column_index]]].max(skipna=True, ), "\n")


def run():
    matrix = createMatrix()
    matrix_with_noise = make_noise(matrix)

    uploadCSV(matrix_with_noise)
    downloadCSV(tableName)

    max(tableName, 2)
    min(tableName, 2)
    avg(tableName, 2)
    median(tableName, 2)


run()

