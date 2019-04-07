# Lee los números del
# archivo y los vuelca
# en un vector

def read_data(path):

    data = []

    with open(path) as f:
        n = f.readline()
        data.put(n)

    return data

