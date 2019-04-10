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

def producto(*args, repeat=1):

    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    
    for prod in result:
        yield tuple(prod)

def calcular_permutaciones(data, r=None):

    pool = tuple(data)

    n = len(pool)

    r = n if r is None else r

    # Genera el producto cartesiano
    # y filtra, luego de generar un set,
    # las posibilidades que no tengan como
    # longitud la especificada en 'r' (cantidad
    # de elementos a tomar)
    #
    for indices in producto(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def permutaciones_vector(data, arg):

    # Se filtran los repetidos
    data = list(set(data))

    p = list(calcular_permutaciones(data))
 
    p = [str(perm) for perm in p]

    return ("Permutaciones-Vector", p)

def permutaciones_lista(data, arg):

    return ("Permutaciones-Lista", [])

def permutaciones_vector_ord(data, arg):

    # Se filtran y ordenan los valores
    data = sorted(data)

    p = list(calcular_permutaciones(data))
 
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

