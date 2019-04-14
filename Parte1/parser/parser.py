#! /usr/bin/env python
import sys
import csv

#el archivo se lo corre de la siguiente forma: python3 parser.py [cantidad de jugadores] [nombre del archivo con los jugadores]
# Ej: python3 parser.py 4 jugadores.rank

def crear_diccionario_original(cantidad_jugadores, file_jugadores):
	lista_jugadores = []
	jugadores = open(file_jugadores)
	jugadores_csv = csv.reader(jugadores)
	for jugador in jugadores_csv:
		lista_ranking = []
		ranking = open(jugador[2])
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

def crear_ranking_oferentes(cantidad_jugadores, lista_jugadores):
	ranking_oferentes = {}
	for jugador in lista_jugadores[:int(int(cantidad_jugadores)/2)]:
		candidatos = jugador[1]
		sorted(candidatos, key=getKey)
		lista_de_listas = []
		for candidato in candidatos:
			if not lista_de_listas:
				lista_de_listas.append([candidato[1], [candidato[0]]])
			else:
				if lista_de_listas[-1][0] == candidato[1] :
					lista_de_listas[-1][1].append(candidato[0])
				else:
					lista_de_listas.append([candidato[1], [candidato[0]]])
		ranking_oferentes[jugador[0]] = [getJustValues(item) for item in lista_de_listas]
	return ranking_oferentes

def crear_ranking_candidatos(cantidad_jugadores, lista_jugadores):
	ranking_candidatos = {}
	for jugador in lista_jugadores[int(int(cantidad_jugadores)/2):]:
		candidato = jugador[0]
		oferentes = {}
		for oferente in jugador[1]:
			oferentes[oferente[0]] = oferente[1]
		ranking_candidatos[candidato] = oferentes
	return ranking_candidatos


def main():
	cantidad_jugadores = sys.argv[1]
	jugadores = sys.argv[2]
	lista_jugadores = crear_diccionario_original(cantidad_jugadores, jugadores)
	ranking_oferentes = crear_ranking_oferentes(cantidad_jugadores, lista_jugadores)
	ranking_candidatos = crear_ranking_candidatos(cantidad_jugadores, lista_jugadores)

main()



