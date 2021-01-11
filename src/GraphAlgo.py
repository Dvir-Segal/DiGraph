from encodings import undefined
from tokenize import Double
import numpy as np
import matplotlib.pyplot as plt
import json
from typing import List, Collection
from collections import deque
from src import GraphAlgoInterface, GraphInterface, DiGraph, NodeData
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from collections import defaultdict
from matplotlib.ticker import AutoLocator
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patches as mpatches
import matplotlib
import numpy as np
import math
from math import e
from math import pi
import copy


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph algotirhms class."""
    myGraph = DiGraph()
    tropologicalSort = []
    sccList = []

    def __init__(self, graph=myGraph):  # , graph: DiGraph):
        self.myGraph = DiGraph()
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
            self.myGraph = DiGraph()
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
                json.dump(self.myGraph.as_dict(), indent=4, fp=file)
            return True
        except Exception as e:
            return False
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """

    def shortest_path_list(self, src, dest):
        groupNodes = self.myGraph._nodes  # get and store the graphs' collection of vertices.
        parents = {}  # for (space I guess.. wanted to achieve time) complexity reason-
        # a hashmap of parents, to restore the parent of each node in the shortest path
        myListg = []  # create a list for returning the shortest path.
        #     groupNodes[i.getKey()] = i  # for every key in the nodes list put it in the hashmap with its key.

        desty = dest  # for further use

        if (dest == src):  # the path of node from itself to itself is itself.
            myListg.append(groupNodes.get(src))
            return myListg

        if src not in groupNodes.keys() or dest not in groupNodes.keys():
            return myListg

        groupNodesKeys = groupNodes.keys()
        for key in groupNodesKeys:  # initializing- prepearing the nodes for the proccess.
            (groupNodes.get(key)).setTagB(float('inf'))
            groupNodes.get(key).setInfo("")
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
                if node.getTagB() <= minDist:
                    minDist = node.getTagB()
                    minKey = node.getKey()
                    minNode = node

            q.remove(minNode)
            # for every neighbor of minKey= neinode
            if (self.myGraph.all_out_edges_of_node(minKey)):
                for key in self.myGraph.all_out_edges_of_node(
                        minKey).keys():  # where v has not yet been removed from Q.
                    # edge is type edge_data
                    # get node data from edge_data
                    neinode = self.myGraph._nodes.get(key)  # (NodeData) #typed NodeData
                    # we're taking a node from myGraph, which is the neighbor of MINKEY node,
                    # which is the DEST in the edge between MINKEY and DEST.
                    if (neinode in q):  # where v has not yet been removed from Q.#if it contains the neighbor node
                        dist = minDist + self.myGraph.all_out_edges_of_node(minKey).get(key)
                        if (dist < neinode.getTagB()):
                            (neinode).setTagB(dist)  # it's the path's weight sum, why is it double? #(NodeData)
                            neinode.setInfo(str(minKey))

            minDist = float('inf')
        # done with while loop.
        desty = dest

        while (groupNodes.get(desty)).getTagB() != 0 and groupNodes.get(desty).getInfo() != "":
            # typed NodeData
            # means you haven't yet reached the src because only the src has tag=0 (dist)
            # of 0 from itself.
            # myListg.append(groupNodes.get(desty))
            myListg.append(groupNodes.get(desty))
            desty = int(groupNodes.get(desty).getInfo())  # get the "father"
        # myListg.append(groupNodes.get(src)) <<list of nodes
        myListg.append(groupNodes.get(src))  # list of nodes id
        myListg.reverse()  # reverse the list, 'cuz it came reversed, as we got from the dest to src by parents.
        if myListg[len(myListg) - 1].getKey() != dest:
            myListg.clear()

        return myListg

        """     returns the shortest path between src to dest - as an ordered List of nodes"""

    def shortest_path_dist(self, src, dest):
        if (src == dest):  # the distance from a node to itself is 0.
            return 0

        aj = self.shortest_path_list(src, dest)  # aj is type List
        if not (aj):
            return float('inf')  # EMPTY aj MEANS THERE'S NO PATH FROM SRC TO DEST

        weight = (aj.pop(len(aj) - 1)).getTagB()
        return weight  # with -1 cuz of the edges num, if there are 2 nodes, theres only one edge connecting them

        """returns the length of the shortest path between src to dest"""

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        nodesList = self.shortest_path_list(id1, id2)
        # print("nodes",nodesList)
        nodesKeys = []
        for node in nodesList:
            nodesKeys.append(node.key)
        # print("keys ",nodesKeys)
        dist = self.shortest_path_dist(id1, id2)
        return dist, nodesKeys

    """
    Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    @param id1: The start node id
    @param id2: The end node id
    @return: The distance of the path, a list of the nodes ids that the path goes through
    """

    def connected_component(self, id1: int) -> list:
        if self.get_graph() is None or id1 not in self.get_graph().get_all_v().keys():
            return []
        return self.bfs(self.get_graph(), id1, {})
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """

    def connected_components(self) -> List[list]:
        if self.get_graph() is None or self.get_graph().v_size() == 0:
            return []
        all_the_SCC = []
        has_family = {}
        for key in self.get_graph().get_all_v():
            if key not in has_family.keys():
                all_the_SCC.append(self.bfs(self.get_graph(), key, has_family))
        return all_the_SCC
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """

    def bfs(self, g: DiGraph(), id1: int, has_family: dict) -> list:
        scc = []
        queue = deque()
        v_list = g.get_all_v()
        u = v_list.get(id1)
        family_nodes = {}
        scanned = {}
        queue.append(u)
        scc.append(u.key)
        has_family[u.key] = True
        scanned[u] = True
        while queue:
            u = queue.popleft()
            if u.key in g._edges.keys():
                for key in g.all_out_edges_of_node(u.key).keys():
                    v = g.get_all_v().get(key)
                    if v not in scanned:
                        scanned[v] = True
                        family_nodes[v.key] = True
                        queue.append(v)
        queue.append(g.get_all_v().get(id1))
        scanned.clear()
        while queue:
            u = queue.popleft()
            if g.all_in_edges_of_node(u.key) is not None:
                for key in g.all_in_edges_of_node(u.key).keys():
                    v = g.get_all_v().get(key)
                    if v not in scanned:
                        scanned[v] = True
                        queue.append(v)
                        if key in family_nodes.keys() and key not in scc:
                            scc.append(key)
                            has_family[key] = True
        return sorted(list(dict.fromkeys(scc)))

    """BFS algorithm: this method operates BFS twice: one for the original graph, and the
    second time for reverse graph. After this time we get SCC for specific node"""

    def plot_graph(self) -> None:
        fig, axes = plt.subplots(figsize=(8, 6))
        csfont = {'fontname': 'Comic Sans MS'}
        axes.set_title("Graph Plot", **csfont, fontsize=25)

        for node in self.myGraph._nodes.values():
            plt.scatter(node.pos[0], node.pos[1], s=25, color="red")
            plt.text(node.pos[0], node.pos[1] + 0.0001, str(node.key), color="green", fontsize=8)

        for src in self.myGraph._edges.keys():
            for dest in self.myGraph._edges.get(src).keys():
                x1 = self.myGraph._nodes.get(src).pos[0]
                y1 = self.myGraph._nodes.get(src).pos[1]
                x2 = self.myGraph._nodes.get(dest).pos[0]
                y2 = self.myGraph._nodes.get(dest).pos[1]

                if (self.myGraph._edges.get(dest)):  # if there's a chance for a two directional edge..
                    if (self.myGraph._edges.get(dest).get(src)):  # if there's a two- directional edge
                        srcNode = self.myGraph._nodes.get(src)
                        destNode = self.myGraph._nodes.get(dest)
                        plt.annotate("", xy=(destNode.pos[0], destNode.pos[1]), xytext=(srcNode.pos[0], srcNode.pos[1]),
                                     arrowprops=dict(arrowstyle='<->', color='black'))
                    else:
                        #There's only a one directed edge
                        plt.annotate("", xy=(x1, y1), xytext=(x2, y2),
                                     arrowprops=dict(arrowstyle='->'), color='blue')
                else:  # there's only a one directed edge
                    plt.annotate("", xy= (x1, y1), xytext=(x2, y2), arrowprops=dict(arrowstyle='->', color='blue'))

        white_patch = mpatches.Patch(color='blue', label='(one)Directed edge')
        black_patch = mpatches.Patch(color='black', label='Bidirected edge')
        magenta_patch = mpatches.Patch(color='red', label='Node')
        plt.legend(handles=[black_patch, white_patch, magenta_patch])
        # axes.relim()
        # axes.autoscale_view()
        plt.show()
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
