#
# Devuelve la moda de un 
# conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#   - Heap de máximos
#

from llist import sllist
from heapq import heappop, heappush

def moda_vector(data, arg):

    apariciones = {}

    moda = data[0]
    
    for elemento in data:
        apariciones[elemento] = apariciones.get(elemento, 0) + 1
        moda = moda if apariciones[moda] > apariciones[elemento] else elemento

    return ("Moda-Vector", moda)

def moda_lista(data, arg):

    lista = sllist(data)

    apariciones = {}
    
    moda = lista.first()

    for elemento in lista:
        apariciones[elemento] = apariciones.get(elemento, 0) + 1
        moda = moda if apariciones[moda] > apariciones[elemento] else elemento

    return ("Moda-Lista", moda)

def moda_vector_ord(data, arg):

    data = sorted(data, reverse=True)

    apariciones_actual = 0
    elemento_previo = None
    maxima_aparicion = 0
    moda = None

    for elemento in data:
        if elemento != elemento_previo:
            moda = elemento_previo if maxima_aparicion < apariciones_actual else moda
            maxima_aparicion = apariciones_actual if maxima_aparicion < apariciones_actual else maxima_aparicion
            elemento_previo = elemento
            apariciones_actual = 0
        apariciones_actual += 1

    maxima_aparicion = apariciones_actual if maxima_aparicion < apariciones_actual else maxima_aparicion
    moda = elemento_previo if maxima_aparicion < apariciones_actual else moda

    return ("Moda-Vector-Ordenado", moda)

def moda_heap(data, arg):

    # Se cargan los valores del
    # vector en un 'diccionario' y se guardan
    # como valor un contador que se aumenta
    # cada vez que se encuentre una nueva aparición
    # del mismo elemento -> O(n)
    #
    # Luego se genera un heap de máximos
    # con las tuplas (valor, ocurrencias)
    #   -> O(k*log(k)) con k = cantidad de números
    #                             diferentes.
    # 
    # Finalmente se obtine el primer elemento
    # que es el máximo de ocurrecias -> O(1)
    #
    # Espacio: O(k) [k: cantidad de elementos diferentes
    #    peor caso -> O(n)] + O(n) [vector incial]
    #  -> resultado: O(n)

    d = {}

    for val in data:
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1

    its = list(d.items())

    h = []

    for e in its:
        heappush(h, (-e[1], e[0]))
        
    m = heappop(h)

    moda = m[1]

    return ("Moda-HeapMax", moda)

def moda(data, arg):

    resultado = []

    resultado.append(moda_vector(data, arg))
    resultado.append(moda_lista(data, arg))
    resultado.append(moda_vector_ord(data, arg))
    resultado.append(moda_heap(data, arg))

    return resultado

