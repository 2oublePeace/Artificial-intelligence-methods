import matplotlib.pyplot as plt
import numpy as np
import pandas
from scipy.signal import lfilter


def download_csv(table):
    matrix_frame = pandas.read_csv(table, delimiter=';')
    return matrix_frame


def upload_csv(table, table_path):
    table.to_csv(table_path, sep=';', index=False)


def fillna(matrix):
    for column in matrix.columns.values:
        matrix[column] = matrix[column].fillna(matrix[column].mean(skipna=True))
    return matrix


def denoise(matrix):
    first_quantile = matrix.quantile(q=0.25, numeric_only=True)
    second_quantile = matrix.quantile(q=0.75, numeric_only=True)
    between_edge = np.zeros(4)
    upper_edge = np.zeros(4)
    lower_edge = np.zeros(4)

    for i in range(0, 4):
        between_edge[i] = (second_quantile[i] - first_quantile[i])
        upper_edge[i] = (second_quantile[i] + 1.5 * between_edge[i])
        lower_edge[i] = (first_quantile[i] - 1.5 * between_edge[i])


    index = 0
    for column in matrix.columns.values:
        for j in range(0, matrix.shape[0]):
            if matrix[column].values[j] > upper_edge[index] or matrix[column].values[j] < lower_edge[index]:
                matrix[column].values[j] = matrix[column].mean(skipna=True)
        index = index + 1
        print(index)

    return matrix


def simpleAnalyse(filtered_matrix):
    print("              Weather")
    print("Медиана", filtered_matrix['temperature'].median())
    print("Максимум", filtered_matrix['temperature'].max())
    print("Минимум", filtered_matrix['temperature'].min())


def run():
    table_name = 'weather.csv'
    table_filter_name = 'weather_filtered.csv'

    matrix = download_csv(table_name)
    matrix.rolling(50).mean().plot(figsize=(12, 8))
    plt.axis('off')
    plt.show()
    table_columns = matrix.columns.values
    filtered_matrix = pandas.DataFrame(fillna(denoise(matrix)), columns=table_columns)
    filtered_matrix.rolling(50).mean().plot(figsize=(12, 8))
    plt.axis('off')
    plt.show()
    upload_csv(filtered_matrix, table_filter_name)
    simpleAnalyse(filtered_matrix)


run()
