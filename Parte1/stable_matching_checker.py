
"""
@dev Checker para solucion de una instancia especifica del problema del matcheo estable
@param parejas Diccionario de tuplas donde la clave es el oferente y el valor es el candidato
@param ranking_oferentes Diccionario con oferentes como claves y listas de preferencia como valores
@param ranking_candidatos  Diccionario con candidatos como claves y listas de preferencia como valores
@return es_estable Verdadero si el emparejamiento es estable
"""
def es_matching_estable(parejas, candidatos, ranking_oferentes, ranking_candidatos):
    
    for oferente, candidato in parejas.itervalues():
        if not es_pareja_estable(oferente, candidato, parejas, ranking_oferentes, ranking_candidatos):
            return False
    return True

def es_pareja_estable(oferente, candidato, parejas, ranking_oferentes, ranking_candidatos):

    for mejor_oferente in ranking_candidatos[oferente]:
        candidato_competidor = parejas[mejor_oferente]
        if es_mejor_nueva_opcion(candidato_competidor, mejor_oferente, candidato, ranking_oferentes[mejor_oferente])
            return False
    return True

def es_mejor_nueva_opcion(candidato_actual, oferente_en_conflicto, nueva_opcion_candidato, ranking_oferente):
    for candidato in ranking_oferente:
        if candidato == nueva_opcion_candidato: # Encuentro primero al nuevo candidato
            return True
        if candidato == candidato_actual: # Encuentro primero al que ya tenia
            return False