import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def linear_regression(x, y):
    model = LinearRegression().fit(x, y)
    y_predicted = model.predict(x)
    sns.regplot(x=x, y=y, data=y_predicted, color='red')
    sns.regplot(x=x, y=y_predicted, data=y_predicted, color='green')
    r_sq = model.score(x, y)
    print('Determination coeff', r_sq)
    print('b0:', model.intercept_)
    print('b1:', model.coef_)
    plt.show()


def main():
    data = pd.read_csv("weather_filtered.csv")
    x_vector = np.array(data['temperature']).reshape((-1, 1))
    y_vector = np.array(data['pressure'])
    linear_regression(x_vector, y_vector)


main()
