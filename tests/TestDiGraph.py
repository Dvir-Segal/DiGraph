import unittest
import sys
from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    """
       UnitTest for DiGraph
       """
    global graph

    def setUp(self):
        """
           The method build the central graph for all the tests
           """
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
        self.graph = g


    def test_sizes(self):
        """
        The central graph contains 15 nodes and 9 edges. Total: 24 ganges. With those data we know to track the changes in the graph
        """
        self.assertEqual(15, self.graph.v_size())
        self.assertEqual(9, self.graph.e_size())
        self.assertEqual(24, self.graph.get_mc())



    def test_removeEdge(self):
        """Test for removeEdge: in the graph, the dests of node 3 are nodes 2, 10, 13, and the sources of node 2 are nodes 3, 11.
        1. remove 3-->2 - true
        2. remove 3-->2 - the edge has already removed, false
        3. remove 3-->10 - true
        4. remove 2-->7 - the edge doesn't exist, false
        5. remove 2-->11 - the edge doesn't exist, false
        6. remove 11-->2 - true
        7. remove 21-->5 - node 21 doesn't exist, false

        Now, the graph contains only 6 edges, and it was change more 2 times, total: 27 changes"""

        print("all the dests of node 3: " + str(self.graph.all_out_edges_of_node(3)))
        print("all the srcs of node 2: " + str(self.graph.all_in_edges_of_node(2)))
        print()
        self.graph.remove_edge(3, 2)
        self.graph.remove_edge(3, 2)
        self.graph.remove_edge(3, 10)
        self.graph.remove_edge(2, 7)
        self.graph.remove_edge(2, 11)
        self.graph.remove_edge(11, 2)
        self.graph.remove_edge(21, 5)
        self.assertEqual(15, self.graph.v_size())
        self.assertEqual(6, self.graph.e_size())
        self.assertEqual(27, self.graph.get_mc())
        print("all the update dests of node 3: " + str(self.graph.all_out_edges_of_node(3)))
        print("all the update srcs of node 2: " + str(self.graph.all_in_edges_of_node(2)))
        print()
        print("Initialization of the graph")
        print()
        print()



    def test_removeNode(self):
        """Test for removeNode: in the graph, the dests of node 14 are nodes 5, 8, and the sources of node 9 are nodes 0, 1, 4.
        1. remove node 1 - true. By the way, we remove 1-->9 (2 changes)
        2. remove node 12 - true (1 change)
        3. remove node 8 - true. By the way, we remove 14-->8 (2 changes)
        4. remove node 19 - the node doesn't exist, false
        5. remove node 4 - true. By the way, we remove 4-->9 (2 changes)

        Now, the graph contains only 6 edges, 11 nodes and it was change more 7 times, total: 31 changes"""

        print("all the dests of node 14: " + str(self.graph.all_out_edges_of_node(14)))
        print("all the srcs of node 9: " + str(self.graph.all_in_edges_of_node(9)))
        print()
        self.graph.remove_node(1)
        self.graph.remove_node(12)
        self.graph.remove_node(8)
        self.graph.remove_node(19)
        self.graph.remove_node(4)
        self.assertEqual(11, self.graph.v_size())
        self.assertEqual(6, self.graph.e_size())
        self.assertEqual(31, self.graph.get_mc())
        print("all the update dests of node 14: " + str(self.graph.all_out_edges_of_node(14)))
        print("all the update srcs of node 9: " + str(self.graph.all_in_edges_of_node(9)))
        print()
        print("Initialization of the graph")
        print()
        print()



if __name__ == '__main__':
    unittest.main()