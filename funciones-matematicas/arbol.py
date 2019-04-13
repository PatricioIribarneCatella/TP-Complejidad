#
# Se calculan las permutaciones
# y variaciones (con y sin repetición)
# de 'N' elementos, teniendo en cuenta
# una estructura de árbol auxiliar, la cual
# se genera a partir de los elementos a permutar.
#

class Nodo:

    def __init__(self, val, level, n, filtrar):

        self.val = val
        self.n = n
        self.children = []
        
        if level > 0:
            for i in range(n):
                if i != self.val or not filtrar:
                    self.children.append(Nodo(i, level - 1, n, filtrar))

    def hasChildren(self):
        return len(self.children) > 0

    def getValue(self):
        return self.val

    def getChildren(self):
        return self.children

class Arbol:

    def __init__(self, data, r, filtrar):

        self.data = data
        self.r = r
        self.filtrar = filtrar
        
        self._construir()

    def _construir(self):

        n = len(self.data)

        level = self.r - 1

        self.t = [Nodo(i, level, n, self.filtrar) for i in range(n)]
    
    def _visitar(self, aux, node, r, resultados, filtrar):

        aux.append(node.getValue())

        if node.hasChildren():
            for e in node.getChildren():
                self._visitar(aux, e, r, resultados, filtrar)
            aux.pop()
        else:
            s = set(aux)
            if filtrar:
                if len(s) == r:
                    resultados.append(list(aux))
            else:
                resultados.append(list(aux))
            aux.pop()

    def generar_variaciones(self):

        aux = []
        res = []

        for nodo in self.t:
            self._visitar(aux, nodo, self.r, res, self.filtrar)
    
        var = []

        for comb in res:
            var.append(tuple(self.data[comb[i]] for i in range(len(comb))))

        return var

def calcular_variaciones(data, r=None, filtrar=True):

    n = len(data)

    r = n if r is None else r

    a = Arbol(data, r, filtrar)

    var = a.generar_variaciones()

    return var

