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

def media_vector(data, arg, version):

    media = 0
    cantidad = 0
    
    for elemento in data:
        media += elemento
        cantidad += 1

    media = media/cantidad

    return ("Media-" + version, media)

def media_lista(data, arg):

    return media_vector(data, arg, "Lista")

def media_vector_ord(data, arg):

    return media_vector(data, arg, "Vector-Ordenado")

def media(data, arg):

    resultado = []

    resultado.append(media_vector(data, arg, "Vector"))
    resultado.append(media_lista(data, arg))
    resultado.append(media_vector_ord(data, arg))

    return resultado

