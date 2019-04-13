#
# Devuelve el número de permutaciones
# de un conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#   - Arbol (descripto en arbol.py)
#

from data import Vector, Lista
from utils import calcular_variaciones
import arbol as a

def permutaciones_vector(data, arg):

    data = Vector(data)

    p = list(calcular_variaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Vector", p)

def permutaciones_lista(data, arg):

    data = Lista(data)

    p = list(calcular_variaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Lista", p)

def permutaciones_vector_ord(data, arg):

    # Se ordenan los valores
    data = sorted(data)

    data = Vector(data)

    p = list(calcular_variaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Vector-Ordenado", p)

def permutaciones_arbol(data, arg):

    p = a.calcular_variaciones(data)

    p = [str(perm) for perm in p]

    return ("Permutaciones-Arbol", p)

def permutaciones(data, arg):

    resultados = []

    # Se filtran los repetidos
    data = list(set(data))

    resultados.append(permutaciones_vector(data, arg))
    resultados.append(permutaciones_lista(data, arg))
    resultados.append(permutaciones_vector_ord(data, arg))
    resultados.append(permutaciones_arbol(data, arg))

    return resultados

