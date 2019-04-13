import unittest
import random

from gale_shapley_weak_ties import gale_shapley
from stable_matching_checker import es_matching_estable
from collections import deque

class BasicGaleShapley(unittest.TestCase):
    def test_basic_gale_shapley_simple_case_and_checker(self):

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

        solucion = gale_shapley(ranking_oferentes.keys(), ranking_candidatos.keys(), ranking_oferentes, ranking_candidatos)
        self.assertTrue(es_matching_estable(solucion, ranking_oferentes, ranking_candidatos))

    def random_groups(self, sequence):
        random_sequence = random.sample(sequence, len(sequence))
        group_sequence = []
        i, f = (0, random.randint(1,len(sequence)))
        while (i < len(sequence)):
            group_sequence.append(random_sequence[i:f])
            i, f = (f, random.randint(f+1,max(f+1,len(sequence))))
        
        return group_sequence

    def test_gale_shapley_multiple_big_cases_with_checker(self):
        for i in range(200):

            cantidad_oferentes = 20
            cantidad_candidatos = 20
            random.seed(i)
            
            oferentes = list(range(0, cantidad_oferentes))
            candidatos = list(range(0, cantidad_candidatos))
            puntajes_posibles = [random.randrange(cantidad_oferentes) for i in range(cantidad_oferentes)] 

            list(range(1, cantidad_oferentes + 1))
            
            ranking_candidatos = {}
            for candidato in candidatos:
                ranking_candidatos[candidato] = random.sample(puntajes_posibles, len(puntajes_posibles))
            
            ranking_oferentes = {}

            for oferente in oferentes:
                ranking_oferentes[oferente] = self.random_groups(oferentes)
                
            ranking_oferentes_colas = {}
            for oferente, ranking in ranking_oferentes.items():
                ranking_oferentes_colas[oferente] = deque(ranking)

            solucion = gale_shapley(oferentes, candidatos, ranking_oferentes_colas, ranking_candidatos)
            self.assertTrue(es_matching_estable(solucion, ranking_oferentes, ranking_candidatos))


if __name__ == '__main__':
    unittest.main()
