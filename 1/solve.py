import matplotlib.pyplot as plt
import statistics
from mat_stat1 import file_read_service


# Выборочное среднее
def get_mean_data(data):
    return statistics.mean(data)


# Выборочная дисперсия
def get_variance_data(data):
    mean = get_mean_data(data)
    sum = 0
    for elem in data:
        sum += (mean - elem) ** 2
    return sum / len(data)


# Стандартное отклонение
def get_standart_dev_data(data):
    return get_variance_data(data) ** (0.5)


# Выборочный коэффициент асимметрии
def get_asymmetry_data(data):
    mean = get_mean_data(data)
    standart_dev = get_standart_dev_data(data)
    sum = 0
    for elem in data:
        sum += (elem - mean) ** 3
    return sum / standart_dev ** 3


# Выборочный коэффициент эксцесса
def get_exc_koef_data(data):
    mean = get_mean_data(data)
    standart_dev = get_standart_dev_data(data)
    sum = 0
    for elem in data:
        sum += (elem - mean) ** 4
    return sum / standart_dev ** 4 - 3


# Построение гистограммы
def draw_hist(data_one, data_two):
    fix, ax = plt.subplots(1, 2)
    ax[0].hist(data_one, bins=len(data_one))
    ax[0].set_title('Гистограмма первой выборки')
    ax[1].hist(data_two, bins=len(data_two))
    ax[1].set_title('Гистограмма второй выборки')
    plt.show()


if __name__ == '__main__':
    FILE_NAME = 'data.txt'

    data_one, data_two = file_read_service.get_data_from_file_vertical(FILE_NAME)

    print('Выборочное среднее для первой выборки: ' + str(get_mean_data(data_one)))

    print('Выборочная дисперсия для первой выборки: ' + str(get_variance_data(data_one)))

    print('Выборочный коэффициент асимметрии для первой выборки: ' + str(get_asymmetry_data(data_one)))

    print('Выборочный коэффициент эксцесса для первой выборки: ' + str(get_exc_koef_data(data_one)) + '\n')

    print('Выборочное среднее для второй выборки: ' + str(get_mean_data(data_two)))

    print('Выборочная дисперсия для второй выборки: ' + str(get_variance_data(data_two)))

    print('Выборочный коэффициент асимметрии для первой выборки: ' + str(get_asymmetry_data(data_two)))

    print('Выборочный коэффициент эксцесса для второй выборки: ' + str(get_exc_koef_data(data_two)))

    draw_hist(data_one, data_two)
