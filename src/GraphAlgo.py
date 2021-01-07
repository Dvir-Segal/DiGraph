from encodings import undefined
from tokenize import Double
import json
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from collections import defaultdict
import copy


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph algotirhms class."""
    myGraph = DiGraph()
    tropologicalSort = []
    sccList = []

    # def __init__(self):  # , graph: DiGraph):  # self.myGraph = graph
    #     self.__myGraph= DiGraph()

    def __init__(self, graph=myGraph):  # , graph: DiGraph):
        # self.reversedGraph = DiGraph()
        self.myGraph = graph
        self.tropologicalSort = []  # have the list in tropoligical sort
        self.sccList = [];
        """Init the graph on which this set of algorithms operates on."""

    def get_graph(self) -> DiGraph:
        return self.myGraph

    def get_graph_in_class(self) -> DiGraph:
        return self.myGraph

        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
            self.__init__()
            for n in data.get("Nodes"):
                self.myGraph.add_node(n.get("id"), n.get("pos"))
            for e in data.get("Edges"):
                self.myGraph.add_edge(e.get("src"), e.get("dest"), e.get("w"))
            return True
        except Exception as e:
            return False
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump(self.myGraph.as_dict(),indent=4, fp=file)
            return True
        except Exception as e:
            return False
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """

    def shortest_path_a(self, src, dest):
        groupNodes = self.myGraph._nodes  # get and store the graphs' collection of vertices.
        # groupNodes = copy.deepcopy(self.myGraph.nodes)  # maybe use deepCopy
        parents = {}  # for (space I guess.. wanted to achieve time) complexity reason-
        # a hashmap of parents, to restore the parent of each node in the shortest path
        myListg = []  # create a list for returning the shortest path.
        # list = self.myGraph.getNode  # put the nodes in an arraylist.
        # groupNodes = {}  # create a new nodes hashmap for the actions required.
        # list= listy.values()
        # for i in list:  # i type: NodeData
        #     groupNodes[i.getKey()] = i  # for every key in the nodes list put it in the hashmap with its key.

        desty = dest  # for further use

        if (dest == src):  # the path of node from itself to itself is itself.
            myListg.add(groupNodes.get(src))
            return myListg

        if src not in groupNodes.keys() or dest not in groupNodes.keys():
            #   if (!groupNodes.containsKey(src)||!groupNodes.containsKey(dest)):
            # if one of them doesn't exist there's no path
            #         System.out.println("someone doesnt exist")
            return myListg

        groupNodesKeys = groupNodes.keys()
        for key in groupNodesKeys:  # initializing- prepearing the nodes for the proccess.
            print("key is", key)
            # print("type is ", self.myGraph.get_all_v().get(0))

            # {0: {@343534536}}
            # print("ze", self.myGraph.get_all_v())
            # # self.myGraph.get_all_v().get(0).setInfo("")
            # print("type is ", type(self.myGraph._nodes.get(key)))
            # print("type is ", type(self.myGraph._nodes.get(key).getInfo()))
            # print("setting pos", self.myGraph._nodes.get(key).pos)
            # print("setting info", self.myGraph._nodes.get(key).setInfo("lala"))
            # print("getting info", self.myGraph._nodes.get(key).getInfo())
            # # get_node(key).setInfo("")  # previous node, that from it we got to this node,
            # print("nana")
            # in the shortest path: is an empty string because we didn't start the paving yet
            (groupNodes.get(key)).setTagB(float('inf'))
            # Shortest distance- we set it to infinity cuz we didn't check it yet
            parents[key] = None  # None because initially, we don't have any path to reach

        (groupNodes.get(src)).setTagB(0)
        # distance a node to itelf is 0, and it's the distance of src from itself

        q = deque()  # deque
        groupNodesKeys = groupNodes.keys()
        for key in groupNodesKeys:
            # all nodes in the graph are unoptimized - thus are in Q
            # key is Integer
            q.append(groupNodes.get(key))

        minDist = float('inf')  # double
        minKey = -1  # int
        dist = 0  # double
        minNode = None  # node_data

        while q:  # while it's not empty
            for node in q:  # getting the smallest dist node
                # node is type NodeData
                # System.out.println("key is"+node.getKey())
                if node.getTagB() <= minDist:
                    minDist = node.getTagB()
                    minKey = node.getKey()
                    minNode = node

            q.remove(minNode)
            # for every neighbor of minKey= neinode
            print("luli", self.myGraph)
            if (self.myGraph.all_out_edges_of_node(minKey)):
                for key in self.myGraph.all_out_edges_of_node(
                        minKey).keys():  # where v has not yet been removed from Q.
                    # edge is type edge_data
                    # get node data from edge_data
                    neinode = self.myGraph._nodes.get(key)  # (NodeData) #typed NodeData
                    # we're taking a node from myGraph, which is the neighbor of MINKEY node,
                    # which is the DEST in the edge between MINKEY and DEST.
                    if (neinode in q):  # where v has not yet been removed from Q.#if it contains the neighbor node
                        #   if(getGraph().getEdge(edge.getKey(), minKey)!=-1)  should be^^ for
                        print("nnn", self.myGraph.all_out_edges_of_node(minKey))
                        print("lll", neinode)
                        print(type(neinode))
                        print("pupu", self.myGraph.all_out_edges_of_node(minKey).get(key))
                        dist = minDist + self.myGraph.all_out_edges_of_node(minKey).get(key)
                        # getEdge(minKey, neinode.getKey()).getWeight()  # alt = dist[u] + dist_between(u, v) #check
                        if (dist < neinode.getTagB()):
                            (neinode).setTagB(dist)  # it's the path's weight sum, why is it double? #(NodeData)
                            # because it's requested like that. TO GO THROUGH LATER
                            neinode.setInfo(str(minKey))

            minDist = float('inf')
        # done with while loop.
        desty = dest

        while (groupNodes.get(desty)).getTagB() != 0 and groupNodes.get(desty).getInfo() != "":
            # typed NodeData
            # means you haven't yet reached the src because only the src has tag=0 (dist)
            # of 0 from itself.
            myListg.append(groupNodes.get(desty))
            desty = int(groupNodes.get(desty).getInfo())  # get the "father"

        myListg.append(groupNodes.get(src))
        myListg.reverse()  # reverse the list, 'cuz it came reversed, as we got from the dest to src by parents.
        if myListg[len(myListg) - 1].getKey() != dest:
            myListg.clear()

        return myListg

        """     returns the shortest path between src to dest - as an ordered List of nodes"""

    def shortest_path_dist(self, src, dest):
        if (src == dest):  # the distance from a node to itself is 0.
            return 0
        aj = self.shortest_path_a(src, dest)  # aj is type List
        if not (aj):
            return -1  # EMPTY aj MEANS THERE'S NO PATH FROM SRC TO DEST

        weight = (aj.pop(len(aj) - 1)).getTagB()
        return weight  # with -1 cuz of the edges num, if there are 2 nodes, theres only one edge connecting them
        """returns the length of the shortest path between src to dest"""

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        print("achu ", self.myGraph)
        nodesList = self.shortest_path_a(id1, id2)
        dist = self.shortest_path_dist(id1, id2)
        return dist, nodesList

    def reverse_graph(self, graph: DiGraph) -> DiGraph:
        reversedGraph = DiGraph()
        NodeData.counter = 0
        for nd in graph.get_all_v():  # Reverse the original graph
            nodeToCopy = graph.get_all_v().get(nd)
            print("nd is ", nd)
            reversedGraph.add_node(nd, nodeToCopy.pos)  # add the nodes to the new graph
        for nd in graph.get_all_v():  # Reverse the original graph
            if graph.all_out_edges_of_node(nd):
                for key in graph.all_out_edges_of_node(nd).keys():
                    src = nd
                    dest = key
                    weight = graph.all_out_edges_of_node(nd).get(key)
                    reversedGraph.add_edge(dest, src, weight)
        print("reversedGraph is :", reversedGraph)
        print("reveresedGraph edges are :", reversedGraph._edges)
        print("original graph is :", graph)
        return reversedGraph

    """
    https://www.cs.huji.ac.il/course/2005/dast/slides/lect14.pdf
    https://cs.stackexchange.com/questions/57495/how-do-we-generate-a-depth-first-forest-from-the-depth-first-search
    SCC algorithm implementation, used pseudocode
    """

    def connected_component(self, id1: int) -> list:
        list = self.connected_components()
        print("aaa is", list)
        for l in list:
            if self.myGraph.get_all_v().get(id1) in l:
                return l

        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """

    # dfs implementation
    def dfs(self, G: DiGraph):
        print("got into dfs")
        print("type is", type(G))
        print(G.v_size())
        print(G.get_all_v())
        vertices = G.get_all_v()
        print("vertices is ", vertices)
        for ver in vertices:
            vertex = NodeData
            print("hello", type(ver))
            vertex = vertices.get(ver)
            print("hahaha", type(vertex))
            vertex.color = "white"
            vertex.parent = None
        for ver in vertices:
            vertex = vertices.get(ver)
            if vertex.color == "white":
                self.DFSVISIT(G, vertex)

    """dfs implementation- first part"""

    def DFSVISIT(self, G: DiGraph, vertex: NodeData):
        print("got into DFSVISIT ")
        vertex.color = "gray"
        print(type(vertex.getKey()))
        print(vertex.getKey())
        print("the dict is", G.all_out_edges_of_node(vertex.getKey()))
        allOutEdges = G.all_out_edges_of_node(vertex.getKey())
        allNodes = G.get_all_v()
        print("ggg", G)
        if allOutEdges:
            print("hhh", allOutEdges.keys())
            for vint in allOutEdges.keys():
                print("allNodes", allNodes)
                v = allNodes.get(vint)
                if v.color == "white":
                    v.parent = vertex
                    self.DFSVISIT(G, v)
        vertex.color = "black"
        print("tropological", self.tropologicalSort)
        self.tropologicalSort.append(vertex)

    """dfs implementation- second part"""

    def dfsTropologic(self, G: DiGraph):
        for vertex in self.tropologicalSort:
            print("got into dfsTropologic ")
            vertex.color = "white"
            vertex.parent = None
            G.get_all_v().get(vertex.key).color = "white"
            G.get_all_v().get(vertex.key).parent = None
        for vertex in self.tropologicalSort:
            print(vertex.color)
            if vertex.color == "white":
                print("key is", vertex.key, " want it to be 8")
                scc = []
                scc = self.DFSVISITTropoligic(G, vertex, scc)
                if scc:
                    print("did we")
                    self.sccList.append(scc)
        return self.sccList

    """dfs implementation on the tropolical list of nodes- first part"""

    def DFSVISITTropoligic(self, Ga: DiGraph, vertex, scc):
        print("lucky", vertex)
        print("luckytype", type(Ga))
        #       print(Ga.all_out_edges_of_node(vertex.key))
        print("shouldbeNodeData:", type(vertex))
        vertex.color = "gray"
        # print("hana ", G.all_out_edges_of_node(vertex.key))
        allOut = {}
        print(Ga)
        allOut = Ga.all_out_edges_of_node(vertex.key)
        allNodes = Ga.get_all_v()
        print("pupa")
        if allOut:
            print("nuka")
            for vin in allOut.keys():
                v = allNodes.get(vin)  # get the NodeData
                print("I got in")
                if v.color == "white":
                    print("papa")
                    v.parent = vertex
                    print("Ga type is ", type(Ga))
                    #    def DFSVISITTropoligic(self, Ga: DiGraph, vertex, scc):
                    self.DFSVISITTropoligic(Ga, v, scc)
                    scc.append(v)
        else:
            if not Ga.all_in_edges_of_node(vertex.key):
                scc.append(vertex)  # to add lonely vertices
        if scc:  # if the list of components is not empty
            print("scc is : ", scc)
            return scc
        vertex.color = "black"

        """dfs implementation on the tropolical list of nodes- second part"""

    def connected_components(self) -> List[list]:
        self.dfs(self.myGraph)  # makes the tropological sort of nodes
        print("my vertices are ", self.myGraph.get_all_v())
        print("tropological sort is ", self.tropologicalSort)
        print("maGraph is ", self.myGraph)
        reveredGraph = self.reverse_graph(self.myGraph)
        self.dfsTropologic(reveredGraph)
        print("sccList is: ", self.sccList)
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
