from solution_methods import get_solution_differences, get_solution_text


def _get_difference_between(text1, text2):
    # PARAM text1: un texto
    # PARAM text2: otro texto
    # RETURN: la cantidad de caracteres diferentes entre text1 y text2

    return sum(1 for t1, t2 in zip(text1, text2) if t1 != t2)


def calculate_solution_differences(solution_text, texts):
    # PARAM solution_text: un texto
    # PARAM texts: una lista de textos
    # RETURN: una lista en la que en cada posicion de la misma se guardara la diferencia de caracteres entre el texto
    # de la solucion y el texto que se ubica en dicha posicion en la lista de textos

    differences = []
    for text in texts:
        differences.append(_get_difference_between(solution_text, text))
    return differences


def calculate_neighbor_differences(neighbor_text, solution, texts, modified_position):
    # PARAM neighbor_text: el texto de un vecino a la solucion
    # PARAM solution: una tupla que representa la solucion
    # PARAM texts: una lista de textos
    # PARAM modified_position: la posicion en donde se encuentra el unico caracter diferente del vecino con respecto
    # al texto de la solucion
    # RETURN: una lista en la que en cada posicion de la misma se guardara la diferencia de caracteres entre el texto
    # del vecino y el texto que se ubica en dicha posicion de la lista de textos

    solution_character_in_that_position = get_solution_text(solution)[modified_position]
    neighbor_character_in_that_position = neighbor_text[modified_position]

    solution_differences = get_solution_differences(solution)
    neighbor_differences = []

    for text_number in range(len(texts)):
        text_character = texts[text_number][modified_position]
        solution_value_for_text = solution_differences[text_number]

        if text_character == solution_character_in_that_position:
            neighbor_differences.append(solution_value_for_text + 1)
        elif text_character == neighbor_character_in_that_position:
            neighbor_differences.append(solution_value_for_text - 1)
        else:
            neighbor_differences.append(solution_value_for_text)

    return neighbor_differences
