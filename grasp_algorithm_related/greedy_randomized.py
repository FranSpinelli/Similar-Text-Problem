import math
import random
from collections import Counter
from grasp_algorithm_related.value_calculation import calculate_solution_differences


def _calculate_candidates_list_size(alphabet):
    # PARAM alphabet: una lista que representa un alfabeto
    # RETURN: el tamaño que debería tener la lista de caracteres candidatos posibles en base al tamaño del alfabeto

    result = math.ceil(math.sqrt(len(alphabet)))
    return result


def _get_most_frequent_chars(frequencies, candidates_list_size):
    # PARAM frequencies: Counter donde se almacenan los caracteres y la cantidad de apariciones de los mismos en una
    # determinada posicion de todos los textos
    # PARAM candidates_list_size: el tamaño que debe tener la lista de candidatos
    # RETURN: una lista de candidatos con los caracteres con mas apariciones en determinada posicion de todos los textos

    most_frequent_chars = frequencies.most_common(candidates_list_size)
    return [caracter for caracter, _ in most_frequent_chars]


def generate_most_similar_text(text_list, used_alphabet):
    # PARAM text_list: una lista de textos
    # PARAM used_alphabet: una lista que representa el alfabeto utilizado en dicha lista de textos
    # RETURN: Una tupla solucion compuesta por el texto generado mas parecido a los textos de la lista de texto
    # y las diferencias entre este y dichos textos

    text_length = len(text_list[0])
    candidates_list_size = _calculate_candidates_list_size(used_alphabet)

    result = []

    for text_position in range(text_length):
        frequencies = Counter()
        for text in text_list:
            char = text[text_position]
            frequencies[char] += 1

        most_frequent_chars = _get_most_frequent_chars(frequencies, candidates_list_size)
        selected_char = random.choice(most_frequent_chars)

        result.append(selected_char)

    generated_text = ''.join(result)
    differences = calculate_solution_differences(generated_text, text_list)

    return generated_text, differences
