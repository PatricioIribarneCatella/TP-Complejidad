import unittest
import random

from gale_shapley import gale_shapley
from stable_matching_checker import es_matching_estable
from collections import deque

class BasicGaleShapley(unittest.TestCase):
    def test_basic_gale_shapley_simple_case_and_checker(self):
        oferentes  = [0,1]
        candidatos = [0,1]

        ranking_oferentes = {
            0: candidatos,
            1: candidatos
        }
        ranking_oferentes_colas = {}
        for oferente, ranking in ranking_oferentes.items():
            ranking_oferentes_colas[oferente] = deque(ranking)

        ranking_candidatos = {
            0: [1,2],
            1: [1,2]
        }

        solucion = gale_shapley(oferentes, candidatos, ranking_oferentes_colas, ranking_candidatos)
        self.assertTrue(es_matching_estable(solucion, ranking_oferentes, ranking_candidatos))

    def test_gale_shapley_multiple_big_cases_with_checker(self):
        for i in range(2000):
            cantidad_oferentes = 20
            cantidad_candidatos = 20
            random.seed(i)
            
            oferentes = list(range(0, cantidad_oferentes))
            candidatos = list(range(0, cantidad_candidatos))
            puntajes_posibles = list(range(1, cantidad_oferentes + 1))
            
            ranking_candidatos = {}
            for candidato in candidatos:
                ranking_candidatos[candidato] = random.sample(puntajes_posibles, len(puntajes_posibles))
            
            ranking_oferentes = {}

            for oferente in oferentes:
                ranking_oferentes[oferente] = random.sample(candidatos, len(candidatos))

            ranking_oferentes_colas = {}
            for oferente, ranking in ranking_oferentes.items():
                ranking_oferentes_colas[oferente] = deque(ranking)

            solucion = gale_shapley(oferentes, candidatos, ranking_oferentes_colas, ranking_candidatos)
            self.assertTrue(es_matching_estable(solucion, ranking_oferentes, ranking_candidatos))





if __name__ == '__main__':
    unittest.main()