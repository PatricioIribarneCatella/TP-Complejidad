#
# Contenedores para los vectores
# y listas, para que se puedan tratar
# de igual forma.
#

from llist import sllist

class Data:

    def __init__(self, items):
        self._items = items

    def size(self):
        return len(self._items)

    def get(self, index):
        pass

class Lista(Data):

    def __init__(self, items):
        super().__init__(sllist(items))

    def get(self, index):
        return self._items.nodeat(index).value

class Vector(Data):

    def __init__(self, items):
        super().__init__(items)

    def get(self, index):
        return self._items[index]

