def get_solution_value(solution):
    # PARAM solution: una tupla solucion donde el primer elemento de la misma representa el texto de dicha solucion y
    # el segundo es una lista de diferencias entre dicho texto y los textos de la instancia del problema
    # RETURN: el valor de dicha solucion

    return max(solution[1])


def get_solution_differences(solution):
    # PARAM solution: una tupla solucion donde el primer elemento de la misma representa el texto de dicha solucion y
    # el segundo es una lista de diferencias entre dicho texto y los textos de la instancia del problema
    # RETURN: la lista de diferencias, la cual cada elemento de esta lista representa la
    # diferencia entre la solucion y el texto de la lista de textos que está en la misma posicion

    return solution[1]


def get_solution_text(solution):
    # PARAM solution: una tupla solucion donde el primer elemento de la misma representa el texto de dicha solucion y
    # el segundo es una lista de diferencias entre dicho texto y los textos de la instancia del problema
    # RETURN: el texto de la misma, contenida en el primer elemento de la tupla

    return solution[0]
