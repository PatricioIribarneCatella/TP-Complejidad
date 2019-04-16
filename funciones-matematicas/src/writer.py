#
# Escribe los resultados
# obtenidos en cada una de las
# implementaciones realizadas
#
# Recibe una lista con elementos
# de la forma: (version, resultado)
#

def write_data(res, path):

    with open(path, "w") as f:
        for e in res:
            f.write(e[0] + ": " + str(e[1]) + "\n")

