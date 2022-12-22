import scipy
import statistics
from mat_stat1 import file_read_service
import numpy


def get_interval_std(data, phi):
    var = statistics.variance(data)
    hi_1 = scipy.stats.chi2.ppf(phi, len(data))
    hi_2 = scipy.stats.chi2.ppf(1 - phi, len(data))
    return len(data) * var / hi_2, len(data) * var / hi_1


def run(file_name, phi):
    data_1, data_2 = file_read_service.get_data_from_file_vertical(file_name)

    interval_mean_1 = scipy.stats.norm.interval(confidence=1.0 - phi, loc=statistics.mean(data_1),
                                                scale=numpy.std(data_1))
    interval_mean_2 = scipy.stats.norm.interval(confidence=1.0 - phi, loc=statistics.mean(data_2),
                                                scale=numpy.std(data_2))
    interval_std_1 = get_interval_std(data_1, phi)
    interval_std_2 = get_interval_std(data_2, phi)
    print("Доверительный интервал среднего для первой выборки: ")
    print(interval_mean_1)
    print("Доверительный интервал дисперсии для первой выборки: ")
    print(interval_std_1)
    print("\n")
    print("Доверительный интервал среднего для второй выборки: ")
    print(interval_mean_2)
    print("Доверительный интервал дисперсии для второй выборки: ")
    print(interval_std_2)


if __name__ == '__main__':
    file_nm = "data.txt"
    p = 0.05

    run(file_nm, p)
