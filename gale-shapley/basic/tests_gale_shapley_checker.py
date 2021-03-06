import unittest
from gale_shapley import gale_shapley
from stable_matching_checker import es_matching_estable
from collections import deque

class BasicGaleShapley(unittest.TestCase):
    def test_basic_gale_shapley_simple_case_checker(self):

        ranking_oferentes = {
            0: [0,1],
            1: [0,1]
        }

        ranking_candidatos = {
            0: [1,2],
            1: [1,2]
        }

        solucion = { 0: 0, 1: 1}
        self.assertTrue(es_matching_estable(solucion, ranking_oferentes, ranking_candidatos))

    def test_simple_inestability_gs_checker(self):

        ranking_oferentes = {
            0: [0,1],
            1: [0,1]
        }

        ranking_candidatos = {
            0: [1,2],
            1: [1,2]
        }

        solucion = { 0: 1, 1: 0}
        self.assertFalse(es_matching_estable(solucion, ranking_oferentes, ranking_candidatos))

if __name__ == '__main__':
    unittest.main()