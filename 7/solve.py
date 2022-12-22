from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from mat_stat1 import file_read_service


def plot_regression_line(x, y, b):
    x = np.array(x)
    y = np.array(y)

    plt.scatter(x, y, color="b", marker="o", s=30)

    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="g")

    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()


def run(file_name, phi):
    data_1, data_2 = file_read_service.get_data_from_file_vertical(file_name)

    stat, p_value = stats.pearsonr(data_1, data_2)
    print("Коэффициент корреляции:", stat)
    linregress = stats.linregress(data_1, data_2)
    print("Коэффициенты регрессии:\nb_0 = {} \nb_1 = {}".format(linregress.intercept, linregress.slope))
    print("Коэфициент значимости: ", linregress.pvalue)
    if linregress.pvalue > phi:
        print("Корреляции между данными нет")
    else:
        print("Корреляция между параметрами есть")
    plot_regression_line(data_1, data_2, [linregress.intercept, linregress.slope])


if __name__ == '__main__':
    file_nm = "data.txt"
    p = 0.05

    run(file_nm, p)
