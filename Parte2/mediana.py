#
# Devuelve la mediana de un 
# conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#

from llist import sllist

def mediana_vector(data, arg):
    
    # Tiempo O(n.log(n))
    # Tamaño O(n + n) -> O(n)

    ordenado = sorted(data)
    mediana = 0

    if len(data) % 2 == 1:
        mediana = ordenado[len(data) // 2]
    else:
        mediana = (ordenado[len(data) // 2 - 1] + ordenado[len(data) // 2]) / 2
    
    return ("Mediana-Vector", mediana)

def mediana_lista(data, arg):

    l = sllist(sorted(sllist(data)))

    if l.size % 2 == 1:
        # Cantidad impar
        for i in range(l.size//2 + 1):
            mediana = l.popleft()
    else:
        # Cantidad par
        for i in range(l.size//2):
            r = l.popleft()
        s = l.popleft()
        mediana = (r + s) / 2

    return ("Mediana-Lista", mediana)

def mediana_vector_ord(data, arg):

    # Como se supone que el
    # vector está ordenado, se puede
    # llamar a la función 'mediana_vector'
    # que ordena el vector

    r = mediana_vector(data, arg)

    return ("Mediana-Vector-Ordenado", r[1])

def mediana(data, arg):

    resultados = []

    resultados.append(mediana_vector(data, arg))
    resultados.append(mediana_lista(data, arg))
    resultados.append(mediana_vector_ord(data, arg))

    return resultados
