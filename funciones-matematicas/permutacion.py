#
# Devuelve el número de permutaciones
# de un conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#   - Diccionario
#

def calcular_permutaciones(data, r=None):
    
    pool = tuple(data)
    
    n = len(pool)
    r = n if r is None else r
    
    if r > n:
        return
    
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    
    yield tuple(pool[i] for i in indices[:r])
    
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def permutaciones_vector(data, arg):

     # Se filtran los repetidos
    data = list(set(data))

    p = list(calcular_permutaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Vector", p)

def permutaciones(data, arg):

    resultados = []

    resultados.append(permutaciones_vector(data, arg))

    return resultados

