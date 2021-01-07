
import random
from src.NodeData import NodeData
from src.GraphInterface import GraphInterface



class DiGraph(GraphInterface):
    """This class represents a graph."""
    global _nodes
    global _edges
    global _counter_edge
    global _mc

    def __init__(self):
        self._nodes = {}
        self._edges = {}
        self._counter_edge = 0
        self._mc = 0
        """
        Constructor
        """

    def v_size(self) -> int:
        return len(self._nodes)
    """
         Returns the number of vertices in this graph
         @return: The number of vertices in this graph
         """

    def e_size(self) -> int:
        for i in self._edges.keys():
            self._counter_edge += len(self._edges.get(i))
        return self._counter_edge

    """
             Returns the number of edges in this graph
             @return: The number of edges in this graph
             """

    def get_all_v(self) -> dict:
        return self._nodes

    """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)"""

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._edges.get(id1)

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)"""

    def all_in_edges_of_node(self, id1: int) -> dict:
        in_edges = {}
        for src in self._edges:
            for dest in self._edges[src]:
                if dest == id1:
                    in_edges[src] = self._edges.get(src).get(dest)
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
        if id1 not in self._nodes.keys() or id2 not in self._nodes.keys() and weight<=0:
            return False
        if id1 in self._edges.keys():
            if id2 in self._edges.get(id1):
                return False
            self._edges.get(id1).update({id2: weight})
            self._mc += 1
            return True
        else:
            self._edges[id1] = {id2: weight}
            self._mc += 1
            return True
    """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._nodes.keys():
            return False
        for i in self._nodes.keys():
            if self._nodes.get(i).pos == pos:
                return False
        n = NodeData()
        # node_dict = {"node":NodeData()}
        if pos is None:
            x, y = random.uniform(0, 50), random.uniform(0, 50)
            tupp = (x, y, 0)
            n.pos = tupp
        else:
            n.pos = pos
        self._nodes[node_id] = n
        self._mc += 1
        return True

    """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added"""

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self._nodes.keys() or node_id2 not in self._nodes.keys():
            return False
        if node_id1 not in self._edges or node_id2 not in self._edges.get(node_id1):
            return False
        del(self._edges[node_id1][node_id2])
        self._mc += 1
        return True

    """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes.keys():
            return False
        if node_id in self._edges.keys():
            self._mc += len(self._edges[node_id])
            del(self._edges[node_id])
        delete = []
        for src in self._edges.keys():
            if node_id in self._edges.get(src).keys():
                delete.append(src)
        for src in delete:
            del self._edges[src][node_id]
            self._mc += 1
        del(self._nodes[node_id])
        self._mc += 1
        return True

    """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
    """


    def __repr__(self):
        rep_graph = {"Edges": self._edges, "Nodes": self._nodes}
        return str(rep_graph)
    """ ToString methode """

    def as_dict(self) -> dict:
        our_graph = {}
        list_edges = []
        list_nodes = []
        for src in self._edges.keys():
            for dest in self._edges.get(src).keys():
                list_edges.append({"src":src,"w":self._edges.get(src).get(dest),"dest":dest})
        our_graph["Edges"] = list_edges
        for id in self._nodes.keys():
            list_nodes.append({"pos":str(self._nodes.get(id).pos[0])+","+str(self._nodes.get(id).pos[1])+","+str(0),"id":id})
        our_graph["Nodes"] = list_nodes
        return our_graph
    """ The methode arranges the graph, by our demand (as json format) """

    def set_mc(self):
        self._mc = 0
    """Initialization the number of changes"""

    def __eq__(self, other) -> bool:
        if (not isinstance(other, DiGraph)):
            return False
        if self.v_size()!=other.v_size() or self.v_size()!=other.v_size():
            return False
        for k in self._nodes.keys():
            if k not in other._nodes.keys():
                return False
            if self.as_dict().get("Nodes")[k].get("pos") == other.as_dict().get("Nodes")[k].get("pos"):
                return False
        if len(self._edges) != len(other._edges):
            return False
        for src in self._edges.keys():
            if src not in other._edges.keys():
                return False
            if len(self._edges.get(src)) != len(other._edges.get(src)):
                return False
            for dest in self._edges.get(src).keys():
                if dest not in other._edges.get(src).keys():
                    return False
                if self._edges.get(src).get(dest) != self._edges.get(src).get(dest):
                    return False
        return True

    """ The methode compares between 2 graphs, by the keys of nodes and their position, and by the pairs (src, dest) of edges and their weights"""


