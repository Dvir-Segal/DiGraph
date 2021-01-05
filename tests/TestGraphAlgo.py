import unittest
import src
from src import GraphInterface
from tokenize import Double
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_getGraph(self) -> GraphInterface:
        """
        Test getGraph method.
        """

    def get_graph_in_class(self) -> DiGraph:
        """
        Test getGraph method.
        """

    def test_load_from_json(self, file_name: str) -> bool:
        """
        Test load to json method
        """

    def test_save_to_json(self, file_name: str) -> bool:
        """
        Test save to json method
        """

    def test_shortest_path_a(self, src, dest):
        """
        Test shortest_path_ method
        """

    def test_shortest_path_dist(self, src, dest):
        """
        Test shortest_path_dist method
        """

    def test_shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Test shortest_path method
        """

    def test_dfs(self, G):
        """
        Test dfs method
        """

    def test_reverse_graph(self) -> DiGraph:
        """
        Test reverse_graph method
        """

    def test_DFSVISIT(self, G, vertex):
        """
        Test DFSVISIT method (first DFS travesal, which updates the tropological list of nodes)
        """

    def test_reverse_graph(self):
        """
        Test reversing the graph method
        """

    def test_dfsTropologic(self, G):
        """
        Test DFS method (on the tropoligcal list of nodes)
        """

    def test_DFSVISITTropoligic(self, G, vertex):
        """
        Test Test DFSVISIT method (on the tropoligcal list of nodes)
        """

    def connected_componentsA(self, id1: int) -> list:
        """
        Test id Finding the Strongly Connected Component(SCC) that node id1 is a part of works OK.
        """

    def connected_componentsB(self) -> list[list]:
        """
        Test if Finding all the Strongly Connected Component(SCC) in the graph works OK.
        """

    def plot_graph(self):
        """
        Test plot_graph method
        """


if __name__ == '__main__':
    unittest.main()
