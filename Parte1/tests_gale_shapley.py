import unittest
from gale_shapley import gale_shapley
from collections import deque

class BasicGaleShapley(unittest.TestCase):
    def test_basic_gale_shapley_simple_case(self):

        oferentes  = [0,1]
        candidatos = [0,1]
        ranking_oferentes = {
            0: deque([0,1]),
            1: deque([0,1])
        }
        ranking_candidatos = {
            0: [1,2],
            1: [1,2]
        }

        self.assertDictEqual(gale_shapley(oferentes, candidatos, ranking_oferentes, ranking_candidatos), \
             {0: 0, 1: 1} )


if __name__ == '__main__':
    unittest.main()