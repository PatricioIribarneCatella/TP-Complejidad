
"""
@dev Checker para solucion de una instancia especifica del problema del matcheo estable
@param parejas Diccionario de tuplas donde la clave es el oferente y el valor es el candidato
@param ranking_oferentes Diccionario con oferentes como claves y listas de candidatos ordenados por preferencia
@param ranking_candidatos  Diccionario con candidatos como claves y listas de puntajes dado a cada oferente, indexado por oferente, menos puntaje implica preferencia
@return es_estable Verdadero si el emparejamiento es estable
"""
def es_matching_estable(parejas, ranking_oferentes, ranking_candidatos):
    for oferente, candidato in parejas.items():
        print(oferente)
        print(candidato)
        print('daf')
        if oferente_cambiaria(oferente, candidato, parejas, ranking_oferentes, ranking_candidatos):
            print(parejas)
            return False
    return True

def oferente_cambiaria(oferente, candidato, parejas, ranking_oferentes, ranking_candidatos):

    for mejor_candidato in ranking_oferentes[oferente]:
        if candidato == mejor_candidato:
            break
        if ranking_candidatos[mejor_candidato][oferente] < ranking_candidatos[mejor_candidato][pareja_actual(mejor_candidato, parejas)]:
            print(oferente)
            print(candidato)
            print(mejor_candidato)
            print(ranking_candidatos[mejor_candidato][oferente])
            print(ranking_candidatos[mejor_candidato][pareja_actual(mejor_candidato, parejas)])
            return True
    return False

def pareja_actual(candidato, parejas):
    for oferente_pareja, candidato_pareja in parejas.items():
        if candidato_pareja == candidato:
            return oferente_pareja
    
    raise Exception('Oferente no encontrado')