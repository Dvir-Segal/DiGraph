import GraphInterface
import random
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    """This class represents a graph."""
    _nodes = {}
    _edges = {}
    _counter_edge = 0
    _mc = 0

    def v_size(self):
        return len(self._nodes)

    """
         Returns the number of vertices in this graph
         @return: The number of vertices in this graph
         """

    def e_size(self) -> int:
        return len(self._edges)

    """
             Returns the number of edges in this graph
             @return: The number of edges in this graph
             """

    def get_all_v(self) -> dict:
        return self._nodes

    """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)"""

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._nodes.get(id1)

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)"""

    def all_in_edges_of_node(self, id1: int) -> dict:
        in_edges = {}
        for src in self._edges:
            for dest in self._edges[src]:
                if dest == id1:
                    in_edges[src] = self._edges[src][dest]
        return in_edges

    """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)"""

    def get_mc(self) -> int:
        return self._mc

    """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self._edges and id1 in self._edges and id2 not in self._edges[id1] and weight > 0:
            self._edges[id1][id2] = weight
            return True
        else:
            return False

    """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._nodes:
            return False
        for i in self._nodes:
            if self._nodes[i]["pos"] == pos:
                return False
        if pos == None:
            self._nodes[node_id]["pos"] = (random.uniform(0, 50), random.uniform(0, 50), 0)
        else:
            self._nodes[node_id]["pos"] = pos
        self._nodes[node_id]["node"] = NodeData()
        return True

    """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added"""

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self._nodes or node_id2 not in self._nodes:
            return False
        if node_id1 not in self._edges or node_id2 not in self._edges[node_id1]:
            return False
        del (self._edges[node_id1][node_id2])
        return True

    """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes:
            return False
        del (self._edges[node_id])
        for src in self._edges:
            del (self._edges[src][node_id])
        del (self._nodes[node_id])
        return True

    """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
    """
