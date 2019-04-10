#
# Devuelve el número de permutaciones
# de un conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#

from utils import calcular_variaciones

def permutaciones_vector(data, arg):

    # Se filtran los repetidos
    data = list(set(data))

    p = list(calcular_variaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Vector", p)

def permutaciones_lista(data, arg):

    return ("Permutaciones-Lista", [])

def permutaciones_vector_ord(data, arg):

    # Se filtran y ordenan los valores
    data = sorted(data)

    p = list(calcular_variaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Vector-Ordenado", p)

def permutaciones(data, arg):

    resultados = []

    # Se filtran los repetidos
    data = list(set(data))

    resultados.append(permutaciones_vector(data, arg))
    resultados.append(permutaciones_lista(data, arg))
    resultados.append(permutaciones_vector_ord(data, arg))

    return resultados

