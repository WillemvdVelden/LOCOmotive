Team: LOCOmotive

Course: Heuristieken

Case: RailNL

Summary:
	We take on this problem by representing the railway map in a graph. For this
we use the package NetworkX(https://networkx.github.io). In main.py define the stations as
nodes, and the connections between stations as edges. We also declare the graph to be a
weighted graph, with 2 types of weights. One type is if a node/edge is critical or non-critical, the other type is the amount of minutes it takes for a train to use an edge
between stations.
In helpers.py we define a few minor functions and classes to be used in main.py.
In visualize.py we define the function draw(), which is used to plot the graph with all
it's nodes, edges and other attributes. This function is also called in main.py.


graph class test from: https://www.python-course.eu/graphs_python.php

plotting via networkx and matplotlib: https://networkx.github.io/documentation/networkx-1.10/examples/drawing/weighted_graph.html