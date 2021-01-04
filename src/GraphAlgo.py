from encodings import undefined
from tokenize import Double
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph
from collections import defaultdict


class DiGraph(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""
    __myGraph = None

    def __init__(self, graph: DiGraph):
        self.myGraph = graph
        """Init the graph on which this set of algorithms operates on."""

    def get_graph(self) -> GraphInterface:
        return self.myGraph

    def get_graph_in_class(self) -> DiGraph:
        return self.myGraph

        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """

    def shortest_path_a(self, src, dest):
        c = self.get_graph().getV()  # get and store the graphs' collection of vertices.
        parents = {}  # for (space I guess.. wanted to achieve time) complexity reason-
        # a hashmap of parents, to restore the parent of each node in the shortest path
        myListg = []  # create a list for returning the shortest path.
        list = self.myGraph.getNode  # put the nodes in an arraylist.
        groupNodes = {}  # create a new nodes hashmap for the actions required.
        for i in list:  # i type: NodeData
            groupNodes.put(i.getKey(), i)  # for every key in the nodes list put it in the hashmap with its key.

        desty = dest  # for further use

        if (dest == src):  # the path of node from itself to itself is itself.
            myListg.add(groupNodes.get(src))
            return myListg

        if src not in groupNodes.keys() or dest not in groupNodes.keys():
            #   if (!groupNodes.containsKey(src)||!groupNodes.containsKey(dest)):
            # if one of them doesn't exist there's no path
            #         System.out.println("someone doesnt exist")
            return myListg

        for key in groupNodes.keys:  # initializing- prepearing the nodes for the proccess.
            groupNodes.get(key).setInfo("")  # previous node, that from it we got to this node,
            # in the shortest path: is an empty string because we didn't start the paving yet
            (groupNodes.get(key)).setTagB(Double.POSITIVE_INFINITY)
            # Shortest distance- we set it to infinity cuz we didn't check it yet
            parents.put(key, None)  # None because initially, we don't have any path to reach

        (groupNodes.get(src)).setTagB(0)
        # distance a node to itelf is 0, and it's the distance of src from itself

        q = deque()  # deque
        for key in groupNodes.keys:
            # all nodes in the graph are unoptimized - thus are in Q
            # key is Integer
            q.add(groupNodes.get(key))

        minDist = Double.POSITIVE_INFINITY  # double
        minKey = -1  # int
        dist = 0  # double
        minNode = None  # node_data

        while q:  # while it's not empty
            for node in q:  # getting the smallest dist node
                # node is type NodeData
                # System.out.println("key is"+node.getKey())
                if (((NodeData)(node)).getTagB() <= minDist):
                    minDist = ((NodeData)(node)).getTagB()
                    minKey = node.getKey()
                    minNode = node

            q.remove(minNode)
            # for every neighbor of minKey= neinode
            for edge in self.myGraph.getE(minKey):  # where v has not yet been removed from Q.
                # edge is type edge_data
                # get node data from edge_data
                neinode = self.myGraph.getNode(edge.getDest())  # (NodeData) #typed NodeData
                # we're taking a node from myGraph, which is the neighbor of MINKEY node,
                # which is the DEST in the edge between MINKEY and DEST.
                if (q.contains(neinode)):  # where v has not yet been removed from Q.#if it contains the neighbor node
                    #   if(getGraph().getEdge(edge.getKey(), minKey)!=-1)  should be^^ for
                    dist = minDist + self.myGraph.getEdge(minKey,
                                                          neinode.getKey()).getWeight()  # alt = dist[u] + dist_between(u, v) #check
                    if (dist < neinode.getTagB()):
                        (neinode).setTagB(dist)  # it's the path's weight sum, why is it double? #(NodeData)
                        # because it's requested like that. TO GO THROUGH LATER
                        neinode.setInfo(str(minKey))

            minDist = Double.POSITIVE_INFINITY
        # done with while loop.
        desty = dest

        while (groupNodes.get(desty)).getTagB() != 0 and groupNodes.get(desty).getInfo() != "":
            # typed NodeData
            # means you haven't yet reached the src because only the src has tag=0 (dist)
            # of 0 from itself.
            myListg.add(groupNodes.get(desty))
            desty = int(groupNodes.get(desty).getInfo())  # get the "father"

        myListg.add(groupNodes.get(src))
        myListg.reverse()  # reverse the list, 'cuz it came reversed, as we got from the dest to src by parents.
        if (myListg.get(myListg.size() - 1).getKey() != dest):
            myListg.clear()

        return myListg

        """     returns the shortest path between src to dest - as an ordered List of nodes"""

    def shortest_path_dist(self, src, dest):
        if (src == dest):  # the distance from a node to itself is 0.
            return 0
        aj = self.shortest_path_a(self, src, dest)  # aj is type List
        if (aj.isEmpty()):
            return -1  # EMPTY aj MEANS THERE'S NO PATH FROM SRC TO DEST
        weight = ((NodeData)(aj.get(aj.size() - 1))).getTagB()

        return weight  # with -1 cuz of the edges num, if there are 2 nodes, theres only one edge connecting them
        """returns the length of the shortest path between src to dest"""

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = self.shortest_path_a(id1, id2)
        dist = self.shortest_path_dist(id1, id2)
        return dist, list

    def reverse_graph(self) -> DiGraph:
        for nd in self.myGraph.getV():  # Reverse the original graph
            self.reversedGraph.addNode(nd)  # add the nodes to the new graph
            for edge in self.myGraph.getE(nd.getKey()):
                src = edge.getSrc()
                dest = edge.getDest()
                self.reversedGraph.connect(dest, src, 1)
                # 1 as a defult weight, as it doesn't matter for this DFS algorithm
        return self.reversedGraph;

    """
    https://www.cs.huji.ac.il/course/2005/dast/slides/lect14.pdf
    https://cs.stackexchange.com/questions/57495/how-do-we-generate-a-depth-first-forest-from-the-depth-first-search
    SCC algorithm implementation, used pseudocode
    """

    def connected_component(self, id1: int) -> list:
        list = self.connected_components()
        for l in list:
            if id1 in list:
                return list

        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """

    tropoligalSort = []  # have the list in tropoligical sort
    sccList = [];

    # dfs implementation
    def dfs(self, G):
        for vertex in self.myGraph.get_all_v():
            vertex.color = "white"
            vertex.parent = None
        for vertex in self.myGraph.get_all_v():
            if vertex.color == "white":
                self.DFSVISIT(vertex)

    """dfs implementation- first part"""

    def DFSVISIT(self, G, vertex):
        vertex.color = "gray"
        for v in self.myGraph.all_out_edges_of_node():
            if v.color == "white":
                v.parent = vertex
                self.DFSVISIT(self, G, v)
        vertex.color = "black"
        self.tropoligalSort = vertex + self.tropoligalSort

    """dfs implementation- second part"""

    def dfsTropologic(self, G):
        for vertex in self.tropoligalSort:
            vertex.color = "white"
            vertex.parent = None
        for vertex in self.myGraph.get_all_v():
            if vertex.color == "white":
                self.DFSVISITTropoligic(vertex)

    """dfs implementation on the tropolical list of nodes- first part"""

    def DFSVISITTropoligic(self, G, vertex):
        scc = []
        vertex.color = "gray"
        for v in self.myGraph.all_out_edges_of_node():
            if v.color == "white":
                v.parent = vertex
                self.DFSVISITTropoligic(self, G, v)
                scc = v + scc
        if scc:  # if the list of components is not empty
            self.sccList.append(scc)
        vertex.color = "black"
        return self.sscList

        """dfs implementation on the tropolical list of nodes- second part"""

    def connected_components(self) -> List[list]:
        self.dfs(self, self.myGraph)
        self.reverse_graph(self, self.myGraph)
        self.dfsTropologic(self, self.reverse_graph())
        return self.sccList
        #  self.kosaraju(self, self.myGraph)
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
