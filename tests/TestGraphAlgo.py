import unittest
from datetime import time
import time
import src
from src import GraphInterface
from tokenize import Double
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra


class MyTestCase(unittest.TestCase):
    global is_not_connected
    global connected
    global algo

    def setUp(self):
        """The method creates 3 graphs for this unittest. connected graph and the other one isn't connected and
        the last one is scc_graph. algo initialized on connected"""
        self.startTime = time.time()
        g = DiGraph()
        for n in range(15):
            g.add_node(n)
        g.add_edge(0, 9, 2.5)
        g.add_edge(1, 9, 6.7)
        g.add_edge(4, 9, 40)
        g.add_edge(3, 10, 7)
        g.add_edge(3, 13, 27)
        g.add_edge(3, 2, 4.5)
        g.add_edge(14, 5, 21)
        g.add_edge(14, 8, 41)
        g.add_edge(11, 2, 17)
        self.is_not_connected = g

        graph = DiGraph()
        for n in range(10):
            graph.add_node(n)
        graph.add_edge(0, 1, 12)
        graph.add_edge(1, 2, 67)
        graph.add_edge(2, 3, 43)
        graph.add_edge(3, 4, 17)
        graph.add_edge(4, 5, 27)
        graph.add_edge(5, 6, 4.5)
        graph.add_edge(6, 7, 21)
        graph.add_edge(7, 8, 41)
        graph.add_edge(8, 9, 11.23)
        graph.add_edge(9, 0, 13.765649959)
        self.connected = graph

        di_graph = DiGraph()
        for n in range(10):
            di_graph.add_node(n)
        di_graph.add_edge(0, 1, 13)
        di_graph.add_edge(1, 2, 32)
        di_graph.add_edge(1, 4, 11)
        di_graph.add_edge(2, 3, 12)
        di_graph.add_edge(2, 6, 35)
        di_graph.add_edge(3, 2, 7)
        di_graph.add_edge(3, 7, 21)
        di_graph.add_edge(4, 0, 10)
        di_graph.add_edge(4, 5, 47)
        di_graph.add_edge(5, 6, 31)
        di_graph.add_edge(5, 8, 91)
        di_graph.add_edge(6, 5, 0.2)
        di_graph.add_edge(7, 3, 29)
        di_graph.add_edge(7, 6, 61)
        di_graph.add_edge(8, 5, 22)
        di_graph.add_edge(9, 8, 75)
        self.scc_graph = di_graph

        self.algo = GraphAlgo(self.connected)


    def tearDown(self):
        """This method is activated after eatch test is done, to calculate the time it ran"""
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_save_load(self):
        """Initialization algo on Connected. Then, save Connected in file whose name is "OurGraph".
        After this, replace the graph of algo to is_not_onnected.
        Load algo on "myGraph" file. Now, algo operates Connected again, instead of is_not_onnected."""

        print("algo is operating now on connected:" + str(self.algo.get_graph().as_dict()))
        print()
        self.assertFalse(self.algo.save_to_json(""))
        self.assertTrue(self.algo.save_to_json("OurGraph"))
        self.algo.__init__(self.is_not_connected)
        print("algo is operating now on is_not_connected:" + str(self.algo.myGraph.as_dict()))
        print()
        self.assertFalse(self.algo.load_from_json(""))
        self.assertFalse(self.algo.load_from_json("fakefile"))
        self.assertTrue(self.algo.load_from_json("OurGraph"))
        print(str(self.algo.myGraph))
        print(str(self.is_not_connected))
        self.assertFalse(self.algo.get_graph().__eq__(self.is_not_connected))
        self.assertTrue(self.algo.get_graph().__eq__(self.connected))
        print("algo is operating now on connected:" + str(self.algo.myGraph.as_dict()))
        print()
        self.algo.plot_graph()

    def test_shortest_path_list(self):
        """Creating a graph and checking the shortestPathDist on it"""

        print("Checking shortest_path_list... ")
        g1 = DiGraph()
        for i in range(0, 5):
            g1.add_node(i)
        g1.add_edge(0, 1, 2.5)
        g1.add_edge(0, 1, 20)
        g1.add_edge(1, 2, 6.7)
        g1.add_edge(2, 3, 40)
        g1.add_edge(3, 4, 10)
        g1.add_edge(4, 3, 1)
        g1.add_edge(3, 2, 16)
        g1.add_edge(2, 1, 0.5)
        g1.add_edge(1, 0, 20)
        g1.add_edge(4, 2, 70)
        g1.add_edge(2, 4, 70)
        g1.add_edge(1, 2, 100)
        g1.add_edge(3, 1, 80)
        g1.add_edge(1, 3, 80)

        operator = GraphAlgo(g1)
        self.assertEqual([1], operator.shortest_path(1, 1)[1])
        self.assertEqual([0, 1, 2], operator.shortest_path(0, 2)[1])
        self.assertEqual([0, 1, 2, 3], operator.shortest_path(0, 3)[1])
        self.assertEqual([0, 1, 2, 3, 4], operator.shortest_path(0, 4)[1])
        self.assertEqual([4, 3], operator.shortest_path(4, 3)[1])
        self.assertEqual([4, 3, 2], operator.shortest_path(4, 2)[1])
        self.assertEqual([4, 3, 2, 1], operator.shortest_path(4, 1)[1])
        self.assertEqual([4, 3, 2, 1, 0], operator.shortest_path(4, 0)[1])



    def test_shortest_path_dist(self):
        """Creating a graph and checking the shortestPath on it"""

        print("Checking shortest_path _dist... ")
        g1 = DiGraph()
        for i in range(0, 5):
            g1.add_node(i)
        g1.add_edge(0, 1, 2.5)
        g1.add_edge(0, 1, 20)
        g1.add_edge(1, 2, 6.7)
        g1.add_edge(2, 3, 40)
        g1.add_edge(3, 4, 10)
        g1.add_edge(4, 3, 1)
        g1.add_edge(3, 2, 16)
        g1.add_edge(2, 1, 0.5)
        g1.add_edge(1, 0, 20)
        g1.add_edge(4, 2, 70)
        g1.add_edge(2, 4, 70)
        g1.add_edge(1, 2, 100)
        g1.add_edge(3, 1, 80)
        g1.add_edge(1, 3, 80)

        operator = GraphAlgo(g1)
        self.assertEqual(float('inf'), operator.shortest_path(9, 1)[0])
        self.assertEqual(0, operator.shortest_path(1, 1)[0])
        self.assertEqual(9.2, operator.shortest_path(0, 2)[0])
        self.assertEqual(49.2, operator.shortest_path(0, 3)[0])
        self.assertEqual(59.2, operator.shortest_path(0, 4)[0])
        self.assertEqual(1, operator.shortest_path(4, 3)[0])
        self.assertEqual(17, operator.shortest_path(4, 2)[0])
        self.assertEqual(17.5, operator.shortest_path(4, 1)[0])
        self.assertEqual(37.5, operator.shortest_path(4, 0)[0])


    def test_scc(self):
        """Test for SCC:
        1. print all the SCC's in connected: we have only one SCC, because the graph is connected
        2. init algo on scc_graph
        3. print all the SCC's in scc_graph
        4. print SCC's of 0, 4, 3
        5. check if we have 4 SCC in our graph
        6. check if nodes 6, 8 have same SCC"""

        print("List of all the SCC's in connected :" + str(self.algo.connected_components()))
        self.algo.__init__(self.scc_graph)
        self.algo.plot_graph()
        print("List of all the SCC's in scc_graph :" + str(self.algo.connected_components()))
        print("The SCC of node 0: " + str(self.algo.connected_component(0)))
        print("The SCC of node 4: " + str(self.algo.connected_component(4)))
        print("The SCC of node 3: " + str(self.algo.connected_component(3)))
        self.assertEqual(4, len(self.algo.connected_components()))
        self.assertTrue(True, self.algo.connected_component(6) == self.algo.connected_component(8))


    def test_shortestPathCompare1(self):
        """Runs the shortestPath method from this project's algo, and runs it also through
        netWorkX, to compare results and performance. runs on graph: G_10_80_1.json """

        print("reading from file...", self.algo.load_from_json("G_10_80_1.json"))
        graphnx1 = nx.DiGraph()
        for nodeKey in self.algo.myGraph._nodes.keys():
            graphnx1.add_node(nodeKey)
        for src in self.algo.get_graph()._edges.keys():
            for dest in self.algo.get_graph().all_out_edges_of_node(src).keys():
                graphnx1.add_edge(src, dest, weight= self.algo.get_graph().all_out_edges_of_node(src).get(dest))
        self.startTime = time.time()
        print("shortestPath is ", self.algo.shortest_path(0, 4))
        print("Networx: ")
        print(single_source_dijkstra(graphnx1, 0, 4))
        self.assertEqual(graphnx1.number_of_nodes(), self.algo.myGraph.v_size())

    def test_shortestPathCompare2(self):
        """Runs the shortestPath method from this project's algo, and runs it also through
        netWorkX, to compare results and performance. runs on graph: G_100_800_1.json """

        print("reading from file...", self.algo.load_from_json("G_100_800_1.json"))
        graphnx2 = nx.DiGraph()
        for nodeKey in self.algo.myGraph._nodes.keys():
            graphnx2.add_node(nodeKey)
        for src in self.algo.myGraph._nodes.keys():
            for dest in self.algo.myGraph._edges.get(src).keys():
                graphnx2.add_edge(src, dest, weight= self.algo.myGraph._edges.get(src).get(dest))
        self.startTime = time.time()
        print("shortestPath is ", self.algo.shortest_path(0, 4))
        print("Networx: ")
        print(self.algo.shortest_path(0, 4))
        print(single_source_dijkstra(graphnx2, 0, 4))


    def test_shortestPathCompare3(self):
        """Runs the shortestPath method from this project's algo, and runs it also through
        netWorkX, to compare results and performance. runs on graph: G_1000_8000_1.json """

        print("reading from file...", self.algo.load_from_json("G_1000_8000_1.json"))
        graphnx3 = nx.DiGraph()
        for nodeKey in self.algo.myGraph._nodes.keys():
            graphnx3.add_node(nodeKey)
        for src in self.algo.myGraph._edges.keys():
            for dest in self.algo.myGraph._edges.get(src).keys():
                graphnx3.add_edge(src, dest, weight= self.algo.myGraph._edges.get(src).get(dest))
        self.startTime = time.time()
        print("shortestPath is ", self.algo.shortest_path(0, 4))
        print("Networx: ")
        print(single_source_dijkstra(graphnx3, 0, 4))




    def test_shortestPathCompare4(self):
        """Runs the shortestPath method from this project's algo, and runs it also through
        netWorkX, to compare results and performance. runs on graph:  G_10000_80000_1.json """

        print("reading from file...", self.algo.load_from_json("G_10000_80000_1.json"))
        graphnx4 = nx.DiGraph()
        for nodeKey in self.algo.myGraph._nodes.keys():
            graphnx4.add_node(nodeKey)
        for src in self.algo.myGraph._edges.keys():
            for dest in self.algo.myGraph._edges.get(src).keys():
                graphnx4.add_edge(src, dest, weight= self.algo.myGraph._edges.get(src).get(dest))
        self.startTime = time.time()
        print("shortestPath is ", self.algo.shortest_path(0, 4))
        print("Networx: ")
        print(single_source_dijkstra(graphnx4, 0 , 4))



    def test_shortestPathCompare5(self):
        """Runs the shortestPath method from this project's algo, and runs it also through
        netWorkX, to compare results and performance. runs on graph: G_20000_160000_1.json """

        print("reading from file...", self.algo.load_from_json("G_20000_160000_1.json"))
        graphnx5 = nx.DiGraph()
        for nodeKey in self.algo.myGraph._nodes.keys():
            graphnx5.add_node(nodeKey)
        for src in self.algo.myGraph._edges.keys():
            for dest in self.algo.myGraph._edges.get(src).keys():
                graphnx5.add_edge(src, dest, weight= self.algo.myGraph._edges.get(src).get(dest))
        self.startTime = time.time()
        print("shortestPath is ", self.algo.shortest_path(0, 4))
        print("Networx: ")
        print(single_source_dijkstra(graphnx5, 0, 4))


    def test_shortestPathCompare6(self):
        """Runs the shortestPath method from this project's algo, and runs it also through
        netWorkX, to compare results and performance. runs on graph: G_30000_240000_1.json """

        print("reading from file...", self.algo.load_from_json("G_30000_240000_1.json"))
        graphnx6 = nx.DiGraph()
        for nodeKey in self.algo.myGraph._nodes.keys():
            graphnx6.add_node(nodeKey)
        for src in self.algo.myGraph._edges.keys():
            for dest in self.algo.myGraph._edges.get(src).keys():
                graphnx6.add_edge(src, dest, weight= self.algo.myGraph._edges.get(src).get(dest))
        self.startTime = time.time()
        print("shortestPath is ", self.algo.shortest_path(0, 4))
        print("Networx: ")
        print(single_source_dijkstra(graphnx6, 0, 4))

if __name__ == '__main__':
    unittest.main()
