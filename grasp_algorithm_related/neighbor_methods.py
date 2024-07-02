def get_neighbor_text(neighbor):
    # PARAM solution: una tupla vecino donde el primer elemento de la misma representa el texto de dicho vecino y
    # el segundo es posicion en la cua se diferencia con respecto a una solucion
    # RETURN: el texto de dicho vecino, contenido en el primer elemento de la tupla

    return neighbor[0]


def get_neighbor_modified_position(neighbor):
    # PARAM solution: una tupla vecino donde el primer elemento de la misma representa el texto de dicho vecino y
    # el segundo es posicion en la cua se diferencia con respecto a una solucion
    # RETURN: la posicion en la cual se diferencia de la solucion a la cual es vecino, contenido
    # en el segundo lugar de la tupla

    return neighbor[1]
