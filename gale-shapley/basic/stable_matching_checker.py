
"""
@dev Checker para solucion de una instancia especifica del problema del matcheo estable
@param parejas Diccionario donde la clave es el candidato y el valor es el oferente
@param ranking_oferentes Diccionario con oferentes como claves y listas de candidatos ordenados por preferencia
@param ranking_candidatos  Diccionario con candidatos como claves y listas de puntajes dado a cada oferente, indexado por oferente, menos puntaje implica preferencia
@return es_estable Verdadero si el emparejamiento es estable
"""
def es_matching_estable(parejas, ranking_oferentes, ranking_candidatos):
    for candidato, oferente in parejas.items():
        if oferente_cambiaria(oferente, candidato, parejas, ranking_oferentes, ranking_candidatos):
            return False
    return True

def oferente_cambiaria(oferente, candidato, parejas, ranking_oferentes, ranking_candidatos):
    
    for mejor_candidato in ranking_oferentes[oferente]:
        if candidato == mejor_candidato:
            break
        if ranking_candidatos[mejor_candidato][oferente] < ranking_candidatos[mejor_candidato][parejas[mejor_candidato]]: 
            return True
    return False

