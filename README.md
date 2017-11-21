# LOCOmotive

Course: Heuristieken
Case: RailNL
Teammembers: Mannus Schomaker, Jasper Naberman, Willem van der Velden

We take on this problem by representing the railway map in a graph. For this
we use the package NetworkX (https://networkx.github.io). In main.py define the stations as nodes, and the connections between stations as edges. We also declare the graph to be a weighted graph, with 2 types of weights. One type is if a node/edge is critical or non-critical, the other type is the amount of minutes it takes for a train to use an edge between stations.

In helpers.py we define a few minor functions and classes to be used in main.py.
In visualize.py we define the function draw(), which is used to plot the graph with all it's nodes, edges and other attributes. 
This function is also called in main.py.

### Prerequisites

Use pip to install the requirered packages from requirement.txt

```
pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you have to get a development env running

Install requirements.txt to get all the requirered packages

```
pip install -r requirements.txt
```

And repeat

```

```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system


## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **[Jasper Naberman](https://github.com/jasperNaberman)**
* **[Mannus Schomaker](https://github.com/mannusschomaker)**
* **[Willem van der Velden](https://github.com/WillemvdVelden)**

* **[Wietze Slagman](https://github.com/WietzeSlagman)** - *TechAssist*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* Graph class test from: https://www.python-course.eu/graphs_python.php

* Plotting via networkx and matplotlib: https://networkx.github.io/documentation/networkx-1.10/examples/drawing/weighted_graph.html

