B.S.D
### OPEN SOURCE
### Written in Python

# DiGraph()

## Project - Weighted and undirected graph model - 01/2021 

![a](https://github.com/Dvir-Segal/Ex3Oop/blob/master/pics/graph%20plot1.png)

The project implements a Weighted and directed graph model, using data structures including HashMaps to represent the nodes and neighborhood relationships between them. 

## Don't miss our rich documents!! In this projects DOCS directory.
## Has this graphs whole functions described.

**This project's weighted directed graph functions include:**

* save_to_json- Saving the graph into a file of json
* load()- Loading a graph from a file
* shortestPath()- Find the lighted (the minimal weight of edges) path between two nodes using Dijkstra's algorithm, implemented by a queue
* shortestPathDist()- Returning the shortest path's between two nodes weight
* add(node_data node)- Adding nodes to a graph
* remove(node_data node)- Removing nodes from a graph
* AddEdge(node_data src, node_data dest)- #tochange- Adding neighbors to nodes in the graph- meaning creating an edge between two nodes, starting from the src node to the       dest node
* RemoveEdge(node_data src, node_data dest)- Removing neighbors to nodes in the graph- meaning creating an edge between two nodes, starting from the src node to the dest node
* Receiving the neighbors of a particular junction
* setInfo()- Adding information to the nodes themselves, in two information values ("variables") for each node
* connected componnent(x) - returns the SCC of node x
* connected_componnents() - returns al the SCC componnets in the graph
* all_out_edges_of_node(x) - returns all the dests of x
* all_in_edges_of_node(x) - returns all the srcs of x
* copy()- Deep copy of a graph
* load_from_json()-  Loads a graph from a json file (within a specific structure. id defined in "How to use?".)

The graph contains dict in dict: the keys in the external dict are srcs. Every value is pair of (dest: weight), for an edge.

Tests of this graph include:

# Screenshots from the graph-
## graph tests:
![a](https://github.com/Dvir-Segal/Ex3Oop/blob/master/pics/test1%20graph.png)

![a](https://github.com/Dvir-Segal/Ex3Oop/blob/master/pics/test%20graph%202.png)
