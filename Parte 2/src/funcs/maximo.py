#
# Devuelve el máximo de un 
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

def maximo_vector(data, arg):

    maximo = data[0]

    for elemento in data:
        maximo = max(maximo, elemento)

    return ("Máximo-Vector", maximo)

def maximo_lista(data, arg):

    lista = sllist(data)
    
    maximo = lista.first()
    
    for elemento in lista:
        maximo = max(maximo, elemento)
    
    return ("Máximo-Lista", maximo)

def maximo_vector_ord(data, arg):

    data = sorted(data, reverse=True)

    maximo = data[0]

    return ("Máximo-Vector-Ordenado", maximo)

def maximo_heap(data, arg):

    # Se puede utilizar un Heap de máximos
    # Colocar todos los elementos en el Heap es O(n)
    # Obtener el máximo es O(1)
    #
    # El heap implmentado es de mínimos,
    # para que sea de máximos, se multiplica
    # cada valor por -1 y se invierte el orden.
    # Luego, cuando se retiran se lo vuelve a
    # multiplicar por -1.

    h = []

    for v in data:
        heappush(h, -v)

    maximo = -heappop(h)

    return ("Máximo-HeapMax", maximo)

def maximo(data, arg):

    resultado = []

    resultado.append(maximo_vector(data, arg))
    resultado.append(maximo_lista(data, arg))
    resultado.append(maximo_vector_ord(data, arg))
    resultado.append(maximo_heap(data, arg))

    return resultado

