#
# Devuelve la media de un 
# conjunto de elementos a
# partir de diferentes
# estructuras de datos:
#
#   - Vector
#   - Lista
#   - Vector ordenado de mayor a menor
#

def calcular_media(data):

    media = 0
    cantidad = 0
    
    for elemento in data:
        media += elemento
        cantidad += 1

    media = media/cantidad

    return media

def media_vector(data, arg):

    media = calcular_media(data)

    return ("Media-Vector", media)

def media_lista(data, arg):

    media = calcular_media(data)

    return ("Media-Lista", media)

def media_vector_ord(data, arg):

    media = calcular_media(data)

    return ("Media-Vector-Ordenado", media)

def media(data, arg):

    resultado = []

    resultado.append(media_vector(data, arg))
    resultado.append(media_lista(data, arg))
    resultado.append(media_vector_ord(data, arg))

    return resultado

