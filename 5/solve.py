import scipy
from mat_stat1 import file_read_service
import numpy


def is_f_test(datas, phi, alternative):
    data_1 = numpy.array(datas[0])
    data_2 = numpy.array(datas[1])
    f = numpy.var(data_1, ddof=1) / numpy.var(data_2, ddof=1)
    df1 = data_1.size - 1
    df2 = data_2.size - 1

    if alternative == 'greater':
        p = 1.0 - scipy.stats.f.cdf(f, df1, df2)
    elif alternative == 'less':
        p = scipy.stats.f.cdf(f, df1, df2)
    else:
        p = 2.0 * (1.0 - scipy.stats.f.cdf(f, df1, df2))
    print('p: ', p)
    if p > phi:
        print("Гипотеза о равенстве дисперсий принимается")
    else:
        print("Гипотеза о равенстве дисперсий отклоняется и принимается альтернативная")


def run(file_name, phi):
    data_1, data_2 = file_read_service.get_data_from_file_for_gorizontal(file_name)

    print("Дисперсии распределений, лежащих в основе выборок, неравны.")
    is_f_test((data_1, data_2), phi, "two_sided")
    print('\n')

    print("Дисперсия распределения, лежащего в основе первой выборки, "
          "меньше дисперсии распределения, лежащего в основе второй выборки.")
    is_f_test((data_1, data_2), phi, "less")
    print('\n')

    print("Дисперсия распределения, лежащего в основе первой выборки, "
          "больше дисперсии распределения, лежащего в основе второй выборки.")
    is_f_test((data_1, data_2), phi, "greater")


if __name__ == '__main__':
    file_nm = 'data.txt'
    p = 0.05

    run(file_nm, p)
