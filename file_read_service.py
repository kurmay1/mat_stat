def get_data_from_file_for_gorizontal(file_name):
    data_one = []
    data_two = []

    with open(file_name, 'r') as file:
        line_number = 1
        for line in file:
            mas_line = line.split(" ")
            for elem in mas_line:
                if line_number == 1:
                    data_one.append(float(elem))
                if line_number == 2:
                    data_two.append(float(elem))
            line_number += 1

    return data_one, data_two


def get_data_from_file_vertical(file_name):
    data_one = []
    data_two = []

    with open(file_name, 'r') as file:
        for line in file:
            values = []
            mas_line = line.split(" ")
            for elem in mas_line:
                if elem != '':
                    values.append(elem)
            data_one.append(float(values[0]))
            data_two.append(float(values[1]))

    return data_one, data_two