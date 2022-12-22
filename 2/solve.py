from scipy.stats import chisquare
from mat_stat1 import file_read_service


def is_normal(data, phi):
    statistic, p = chisquare(data)
    print("p-уровень значимости: ", p)
    if p > phi:
        print("Распределение выборки является нормальным")
    else:
        print("Распределение выборки не является нормальным")


if __name__ == '__main__':
    file_nm = 'data.txt'
    p = 0.05

    data_one, data_two = file_read_service.get_data_from_file_vertical(file_nm)

    print("Проверка 1")
    is_normal(data_one, p)

    print("\n")

    print("Проверка 2")
    is_normal(data_two, p)
