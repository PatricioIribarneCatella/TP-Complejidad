#
# Lee los números del
# archivo y los vuelca
# en un vector
#

def read_data(path):

    data = []

    with open(path) as f:
        lines = f.readlines()
        for n in lines:
            data.append(int(n))

    return data

