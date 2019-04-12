from collections import deque

"""
N oferentes, N candidatos

Inicialmente todos estan sin pareja
Mientras haya oferentes libres que no hayan agotados sus opciones (1) 
    Seleccionar O un oferente de 1
    Sea C el candidato de > preferencia de O al que no le propuso
    Si C esa disponible
        (O, C) se comprometen
    Si no
        Sea O' el oferente actual de C
        Si C prefiere a O sobre O'
            (O, C) se comprometen y O' queda libre
"""

# ranking_oferentes diccionario con clave 'oferente' y valor lista ordenada de candidatos
# ranking_candidatos diccionario con clave 'candidato'  y valor diccionario con clave 'oferente' y valor ranking

def gale_shapley(oferentes, candidatos, ranking_oferentes, ranking_candidatos):
    parejas = {}
    oferentes_libres = oferentes[:]
    while (oferentes_libres):
        oferente  = oferentes_libres.pop()
        candidato = ranking_oferentes[oferente][0].pop()
        if not ranking_oferentes[oferente][0]:
            ranking_oferentes[oferente].popleft()
        
        if not candidato in parejas:
            parejas[candidato] = oferente
            continue
        
        oferente_actual = parejas[candidato]
  
        r_oferente, r_oferente_actual = [ranking_candidatos[candidato][o] for o in [oferente, oferente_actual]]
          
        if r_oferente < r_oferente_actual:
            parejas[candidato] = oferente
            oferentes_libres.append(oferente_actual)
        
        else:
            oferentes_libres.append(oferente)
    
    
    return parejas


ranking_oferentes = {
    0: deque([[0],[1],[2],[3]]),
    1: deque([[0],[1,2],[3]]),
    2: deque([[1,3],[0,2]]),
    3: deque([[3],[1,2],[0]])
}

ranking_candidatos = {
    0: {0:1, 1:2, 2:1, 3:1}, 
    1: {0:2, 1:3, 2:3, 3:1},
    2: {0:3, 1:2, 2:1, 3:4},
    3: {0:2, 1:2, 2:1, 3:1}
}

print(gale_shapley(ranking_oferentes.keys(), ranking_candidatos.keys(), ranking_oferentes, ranking_candidatos))
