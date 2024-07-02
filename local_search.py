from solution_methods import *
from neighbor_methods import *
from value_calculation import calculate_neighbor_differences


def _generate_neighborhood(solution_text, alphabet):
    # PARAM solution_text: un texto de la solucion
    # PARAM alphabet: una lista donde cada elemento es un caracter, esta lista representa el alfabeto utilizado
    # RETURN: retorna una lista de tuplas con todos los textos que se pueden generar usando el alfabeto y variando
    # una sola posicion por cada texto, la tupla tendrá en su primer posicion el texto generado y en la segunda
    # la posicion en la que difiere del texto de la solucion

    neighborhood = []

    for text_position in range(len(solution_text)):
        for character in alphabet:
            if character != solution_text[text_position]:
                neighbor = list(solution_text)
                neighbor[text_position] = character
                neighborhood.append((''.join(neighbor), text_position))

    return neighborhood


def _get_best_from_neighborhood(solution_tuple, alphabet, texts):
    # PARAM solution_tuple: una solucion sobre la cual queremos calcular el vecindario
    # PARAM alphabet: el alfabeto utilizado en la lista de textos
    # PARAM texts: una lista de textos
    # RETURN: el vecino de la solucion cuyo valor es el mas bajo, si no hay un vecino
    # con valor mas bajo que el de la solucion, la solucion es retornada

    generated_neighborhood = _generate_neighborhood(get_solution_text(solution_tuple), alphabet)

    for neighbor in generated_neighborhood:
        neighbor_text = get_neighbor_text(neighbor)
        neighbor_differences = calculate_neighbor_differences(neighbor_text, solution_tuple, texts,
                                                              get_neighbor_modified_position(neighbor))

        if max(neighbor_differences) < get_solution_value(solution_tuple):
            return neighbor_text, neighbor_differences

    return solution_tuple


def local_search(first_solution_tuple, alphabet, texts):
    # PARAM first_solution_tuple: una primera solucion de donde arrancar la busqueda local
    # PARAM alphabet: una lista de caracteres que representa el alfabeto utiliado en la lista de textos
    # PARAM texts: una lista de textos
    # RETURN: una solucion minima local

    repetitions_number = 0
    solution_tuple_to_be_returned = first_solution_tuple

    while repetitions_number < 100:
        best_solution_from_neighborhood = _get_best_from_neighborhood(solution_tuple_to_be_returned, alphabet, texts)

        if get_solution_value(best_solution_from_neighborhood) < get_solution_value(solution_tuple_to_be_returned):
            solution_tuple_to_be_returned = best_solution_from_neighborhood
            repetitions_number += 1
        else:
            return solution_tuple_to_be_returned
