#
# Utiliza el algoritmo de 'Heap'
#
# Fuente: https://en.wikipedia.org/wiki/Heap%27s_algorithm
#

def calcular_permutaciones(data):

    r = []
    n = len(data)
    
    c = [0 for i in range(n)]

    r.append(tuple(e for e in data))

    i = 0

    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                data[0], data[i] = data[i], data[0]
            else:
                data[c[i]], data[i] = data[i], data[c[i]]
            r.append(tuple(e for e in data))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return r

def main():

    data = [1,2,3]

    p = calcular_permutaciones(data)

    p = [str(perm) for perm in p]

    print(p)

if __name__ == '__main__':
    main()

