#
# Devuelve el número de variaciones
# de un conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#   - Arbol (descripto en arbol.py)
#

from src.data import Vector, Lista
from src.utils import calcular_variaciones
import src.arbol as a

##################################
########## Variaciones ###########
##################################

def variaciones_vector(data, arg):

    data = Vector(data)

    p = list(calcular_variaciones(data, arg))

    p = [str(perm) for perm in p]

    return ("Variaciones-Vector", p)

def variaciones_lista(data, arg):

    data = Lista(data)

    p = list(calcular_variaciones(data, arg))

    p = [str(perm) for perm in p]

    return ("Variaciones-Lista", p)

def variaciones_vector_ord(data, arg):

    data = sorted(data)

    data = Vector(data)

    p = list(calcular_variaciones(data, arg))

    p = [str(perm) for perm in p]

    return ("Variaciones-Vector-Ordenado", p)

def variaciones_arbol(data, arg):

    p = a.calcular_variaciones(data, arg)

    p = [str(perm) for perm in p]

    return ("Variaciones-Arbol", p)

##################################
### Variaciones con Repetición ###
##################################

def variaciones_rep_vector(data, arg):

    data = Vector(data)

    p = list(calcular_variaciones(data, arg, filtrar=False))

    p = [str(perm) for perm in p]

    return ("Variaciones-Repetición-Vector", p)

def variaciones_rep_lista(data, arg):

    data = Lista(data)

    p = list(calcular_variaciones(data, arg, filtrar=False))

    p = [str(perm) for perm in p]

    return ("Variaciones-Repetición-Lista", p)

def variaciones_rep_vector_ord(data, arg):

    data = sorted(data)

    data = Vector(data)

    p = list(calcular_variaciones(data, arg, filtrar=False))

    p = [str(perm) for perm in p]

    return ("Variaciones-Repetición-Vector-Ordenado", p)

def variaciones_rep_arbol(data, arg):

    p = a.calcular_variaciones(data, arg, filtrar=False)

    p = [str(perm) for perm in p]

    return ("Variaciones-Repetición-Arbol", p)

def variaciones(data, arg):

    resultados = []

    # Se filtran los resultados repetidos
    data = list(set(data))

    resultados.append(variaciones_vector(data, arg))
    resultados.append(variaciones_lista(data, arg))
    resultados.append(variaciones_vector_ord(data, arg))
    resultados.append(variaciones_arbol(data, arg))

    return resultados
    
def variaciones_rep(data, arg):

    resultados = []

    # Se filtran los resultados repetidos
    data = list(set(data))

    resultados.append(variaciones_rep_vector(data, arg))
    resultados.append(variaciones_rep_lista(data, arg))
    resultados.append(variaciones_rep_vector_ord(data, arg))
    resultados.append(variaciones_rep_arbol(data, arg))

    return resultados

