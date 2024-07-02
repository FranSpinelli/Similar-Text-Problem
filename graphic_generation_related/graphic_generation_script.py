import matplotlib.pyplot as plt


def _read_file(graphic_input_data_file):

    graphic_data_list = []

    with open(graphic_input_data_file, "r") as file:
        for text_line in file:
            run_data = eval(text_line.strip())
            graphic_data_list.append(run_data)

    return graphic_data_list


def generate_graphic_from(graphic_input_data_file):
    plt.figure(figsize=(10, 6))

    run_data_list = _read_file(graphic_input_data_file)
    run_number = 1
    run_stop_condition = ['10', '30', '50', '70']
    x_values = []
    y_values = []

    for run_data in run_data_list:
        iterations = [iteration_value_tuple[0] for iteration_value_tuple in run_data]
        values = [iteration_value_tuple[1] for iteration_value_tuple in run_data]

        plt.plot(iterations, values, label=
        'Corrida ' + str(run_number) + ': Con corte a las ' + run_stop_condition[run_number-1] + ' iteraciones sin mejora')

        plt.axvline(x=iterations[-1], color= 'black', linestyle='--', linewidth=0.5)

        x_values.append(iterations[-1])
        y_values += values

        run_number += 1

    plt.xticks(x_values)
    plt.yticks(list(set(y_values)))

    plt.xlabel('Cantidad de Iteraciones')
    plt.ylabel('Mejor valor obtenido hasta el momento')
    plt.title('Mejor valor obtenido por iteración en diferentes corridas del algoritmo, instancia az_20_30_1')
    plt.legend()

    plt.show()
