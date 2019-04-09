#
# Devuelve la desviación estándar
# de un conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#

from math import sqrt
from media import calcular_media

def ds_vector(data, arg, version):
    
    varianza = 0
    media = calcular_media(data)

    for elemento in data:
        varianza += (media - elemento) ** 2

    varianza = varianza/len(data)
    desvio = sqrt(varianza)

    return ("Desviación-Estándar-" + version, desvio)

def ds_lista(data, arg):

    return ds_vector(data, arg, "Lista")

def ds_vector_ord(data, arg):

    return ds_vector(data, arg, "Vector-Ordenado")

def ds(data, arg):

    resultados = []

    resultados.append(ds_vector(data, arg, "Vector"))
    resultados.append(ds_lista(data, arg))
    resultados.append(ds_vector_ord(data, arg))

    return resultados

