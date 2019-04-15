# Contiene referencias a todas
# las funciones a implementar:
#
#   - Maximo
#   - Media
#   - Mediana
#   - Moda
#   - Desviación estándar
#   - Permutaciones
#   - Variaciones (n,r)
#   - Variaciones con repetición (n,r)
#

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import src.constants as cons

from funcs.maximo import maximo
from funcs.media import media
from funcs.mediana import mediana
from funcs.moda import moda
from funcs.desviacion import ds
from funcs.permutacion import permutaciones
from funcs.variaciones import *

class Functions:

    def __init__(self):

        self._functions = {}
        
        self._functions[cons.MAXIMO] = maximo
        self._functions[cons.MEDIA] = media
        self._functions[cons.MEDIANA] = mediana
        self._functions[cons.MODA] = moda
        self._functions[cons.DS] = ds
        self._functions[cons.PERM] = permutaciones
        self._functions[cons.VAR] = variaciones
        self._functions[cons.VAR_REP] = variaciones_rep

    def get(self, comando):

        cmd = comando.lower()

        if cmd not in self._functions:
            return None

        return self._functions[cmd]
    
    def get_funcs(self):

        return [f for f in self._functions.keys()]

