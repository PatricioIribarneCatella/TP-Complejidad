#! /usr/bin/env python
import sys
import csv
from llist import sllist
from ties_weak.gale_shapley_weak_ties import gale_shapley
from ties_weak.stable_matching_checker import es_matching_estable

#el archivo se lo corre de la siguiente forma: python3 picapica.py [cantidad de jugadores] [nombre del archivo con los jugadores]
# Ej: python3 picapica.py 4 jugadores.rank

def crear_lista_jugadores(cantidad_jugadores, file_jugadores):
	lista_jugadores = []
	jugadores = open("jugadores/%s" % file_jugadores)
	jugadores_csv = csv.reader(jugadores)
	for jugador in jugadores_csv:
		lista_ranking = []
		ranking = open("jugadores/%s" % jugador[2])
		ranking_csv = csv.reader(ranking)
		for persona in ranking_csv:
			lista_ranking.append([persona[0],persona[1]])
		ranking.close()
		lista_jugadores.append([jugador[1],lista_ranking])
	jugadores.close()
	return lista_jugadores


def getKey(item):
	return item[1]

def getJustValues(element):
	return element[1]

def crear_ranking_oferentes(cantidad_jugadores, lista_jugadores, lista_oferentes):
	ranking_oferentes = {}
	for jugador in lista_jugadores[:int(int(cantidad_jugadores)/2)]:
		candidatos = jugador[1]
		sorted(candidatos, key=getKey)
		lista_de_listas = []
		for candidato in candidatos:
			if candidato[0] not in lista_oferentes:
				if not lista_de_listas:
					lista_de_listas.append([candidato[1], [candidato[0]]])
				else:
					if lista_de_listas[-1][0] == candidato[1] :
						lista_de_listas[-1][1].append(candidato[0])
					else:
						lista_de_listas.append([candidato[1], [candidato[0]]])
		ranking_oferentes[jugador[0]] = sllist([getJustValues(item) for item in lista_de_listas])
	return ranking_oferentes

def crear_ranking_candidatos(cantidad_jugadores, lista_jugadores, lista_oferentes):
	ranking_candidatos = {}
	for jugador in lista_jugadores[int(int(cantidad_jugadores)/2):]:
		candidato = jugador[0]
		oferentes = {}
		for oferente in jugador[1]:
			if oferente[0] in lista_oferentes:
				oferentes[oferente[0]] = oferente[1]
		ranking_candidatos[candidato] = oferentes
	return ranking_candidatos

def crear_lista_oferentes(cantidad_jugadores, lista_jugadores):
	lista_oferentes = []
	for jugador in lista_jugadores[:int(int(cantidad_jugadores)/2)]:
		lista_oferentes.append(jugador[0])
	return lista_oferentes

def crear_archivo_salida_gs(parejas):
	f= open("parejas.txt","w")
	for key, value in parejas.items():
		f.write("%s, %s\n" % (key, value))
	f.close()

def crear_archivo_salida_sm(parejas, ranking_oferentes, ranking_candidatos):
	f = open("matching-estable.txt","w")
	resultado = es_matching_estable(parejas, ranking_oferentes, ranking_candidatos)
	f.write(str(resultado))
	f.close()

def entrada_erronea(parametros):
	if len(parametros) != 4:
		return True
	if not parametros[2].isdigit():
		return True
	if parametros[1] not in ["gs", "gale-shapley", "sm", "me", "stable-matching", "matching-estable"]:
		return True
	return False

def main():
	if entrada_erronea(sys.argv):
		print("Error de formato. El formato debe ser picapica.py [funcion] [cantidad de jugadores] [archivo de jugadores]")
	else:
		funcion = sys.argv[1]
		cantidad_jugadores = sys.argv[2]
		jugadores = sys.argv[3]
		lista_jugadores = crear_lista_jugadores(cantidad_jugadores, jugadores)
		lista_oferentes = crear_lista_oferentes(cantidad_jugadores, lista_jugadores)
		ranking_oferentes = crear_ranking_oferentes(cantidad_jugadores, lista_jugadores, lista_oferentes)
		ranking_candidatos = crear_ranking_candidatos(cantidad_jugadores, lista_jugadores, lista_oferentes)
		parejas = gale_shapley(lista_oferentes, ranking_oferentes, ranking_candidatos)
		if funcion in ["gs", "gale-shapley"]:
			crear_archivo_salida_gs(parejas)
		elif funcion in ["sm", "me", "stable-matching", "matching-estable"]:
			crear_archivo_salida_sm(parejas, ranking_oferentes, ranking_candidatos)

main()



