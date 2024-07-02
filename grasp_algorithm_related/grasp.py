from grasp_algorithm_related.greedy_randomized import generate_most_similar_text
from grasp_algorithm_related.local_search import local_search
from grasp_algorithm_related.solution_methods import *
import os


def _read_file(problem_instance_file):
    # PARAM problem_instance_file: el path al archivo que contiene la instancia del problema
    # RETURN: una lista con los textos de dicha instancia

    text_list = []

    with open(problem_instance_file, "r") as file:
        for text_line in file:
            text_line = text_line.strip()
            text_list.append(text_line)

    return text_list


def _write_solution_file(response_file_name, solution):
    # PARAM response_file_name: el nombre del archivo que queremos generar con la solucion
    # PARAM solution: la solucion que queremos guardar en el archivo
    # RETURN: genera un archivo en el directorio "./problem-solutions" en donde la
    # primer linea del archivo es el texto de dicha solucion y la segunda linea es el valor de dicha solucion

    response_file_directory = "./problem-solutions/"
    complete_file_path = os.path.join(response_file_directory, response_file_name)

    with open(complete_file_path, 'w') as file:
        file.write(get_solution_text(solution) + '\n')
        file.write(str(get_solution_value(solution)))


def _generate_file_name_from(problem_instance_file_path):
    # PARAM: problem_instance_file_path: el path del archivo que contiene la instancia del problema sobre la se trabajó
    # RETURN: extrae el nombre del archivo, del path completo, y le agrega el pregijo "solucion-" al mismo,
    # para que luego el archivo con la solucion, lleve ese nombre

    file_name_from_problem_instance_file_path = problem_instance_file_path.split("/")[-1]
    return "solucion_" + file_name_from_problem_instance_file_path


def _determine_alphabet(text_list):
    # PARAM text_list: una lista de textos
    # RETURN: retorna el alfabeto que se utiliza en dichos textos

    return set("".join(text_list))


def grasp(problem_instance_file_path):
    # PARAM problem_instance_file_path: el path completo a donde está el archivo con la instancia del problema
    # con la que vamos a trabajar
    # RETURN: ejecuta el algoritmo GRASP utilizando dicha instancia del problema,
    # genera un nuevo archivo con los resultados de la ejecucion y retorna una tupla donde el primer elemento es el
    # texto de la solucion y el segundo es el valor de la misma

    text_list = _read_file(problem_instance_file_path)
    alphabet = _determine_alphabet(text_list)

    best_solution = None
    iteration = 0
    iterations_without_improvement = 0

    graphic_information = []

    while iterations_without_improvement < 70 and iteration < 100:
        print("iteracion nro: ", iteration)

        # La solucion greedy-randomized solo se utilizará como punto de partida de la busqueda local, ya que esta
        # ultima en el peor de los casos quedará igual que la greedy, en cualquier otro caso siempre lo mejorará
        greedy_randomized_solution = generate_most_similar_text(text_list, alphabet)
        local_search_solution = local_search(greedy_randomized_solution, alphabet, text_list)

        if best_solution is None:
            # En la primer iteracion se asignará la local_search_solution ya que es la mejor hasta el momento
            best_solution = local_search_solution
        elif get_solution_value(local_search_solution) < get_solution_value(best_solution):
            best_solution = local_search_solution
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1

        print("iteraciones sin mejora:", iterations_without_improvement)

        graphic_information.append((iteration, get_solution_value(best_solution)))
        iteration += 1

    _write_solution_file(_generate_file_name_from(problem_instance_file_path), best_solution)

    return graphic_information
