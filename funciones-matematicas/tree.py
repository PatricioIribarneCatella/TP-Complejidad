class Node:

    def __init__(self, val, level, n, filtrar):

        self.val = val
        self.n = n
        self.children = []
        
        if level > 0:
            for i in range(n):
                if i != self.val or not filtrar:
                    self.children.append(Node(i, level - 1, n, filtrar))

    def hasChildren(self):
        return len(self.children) > 0

    def getValue(self):
        return self.val

    def getChildren(self):
        return self.children


def visit(aux, node, r, resultados, filtrar):

    aux.append(node.getValue())

    if node.hasChildren():
        for e in node.getChildren():
            visit(aux, e, r, resultados, filtrar)
        aux.pop()
    else:
        s = set(aux)
        if filtrar:
            if len(s) == r:
                resultados.append(list(aux))
        else:
            resultados.append(list(aux))
        aux.pop()

def perm(data, r, filtrar):

    n = len(data)

    level = r - 1

    t = [Node(i, level, n, filtrar) for i in range(n)]

    aux = []

    resultados = []

    for node in t:
        visit(aux, node, r, resultados, filtrar)

    print("var: {}, len: {}".format(resultados, len(resultados)))

def main():

    perm([1,2,3], 3, True)

if __name__ == "__main__":

    main()

