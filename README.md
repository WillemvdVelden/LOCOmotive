# LOCOmotive

Course: Heuristieken 
Case: RailNL 
Teammembers: Mannus Schomaker, Jasper Naberman, Willem van der Velden 

We take on this problem by representing the railway map in a graph. For this we use the package NetworkX (https://networkx.github.io). 
In main.py define the stations as nodes, and the connections between stations as edges. 
We also declare the graph to be a weighted graph, with 2 types of weights. 
One type is if a node/edge is critical or non-critical, the other type is the amount of minutes it takes for a train to use an edge between stations. 

In this repository you will find several folders, in which there are different files that are imported by main.py. 
In the 'Algorithms'-folder several algorithm functions are located. At the moment some of these are used in main.py. 
In the 'Concepts'-folder older concepts for the solving of this case are located. These are not used by main.py any more. 
In the 'Datafiles'-folder the given .csv-files are located. These are imported in main.py with help from a reader-function from helpers.py. 
In the 'Functions'-folder several 'extra'-functions are located. These are imported and called in main.py. In visualize.py a draw()-function is defined to draw a given graph as a map. In helpers.py functions for csv-reading, score calculation and time calculation are defined. 

## Installing and Prerequisites

Use pip to install the requirered packages from requirement.txt.

```
pip install -r requirements.txt
```

And run
```
python3 main.py
```
to execute to main script for this assignment.

## Authors

* **[Jasper Naberman](https://github.com/jasperNaberman)**
* **[Mannus Schomaker](https://github.com/mannusschomaker)**
* **[Willem van der Velden](https://github.com/WillemvdVelden)**

* **[Wietze Slagman](https://github.com/WietzeSlagman)** - *TechAssist*

See also the list of [contributors](https://github.com/WillemvdVelden/LOCOmotive/graphs/contributors) who participated in this project.

## Acknowledgments

* [Graph class test with the help from Python Course.](https://www.python-course.eu/graphs_python.php)

* [Data structures and plotting via NetworkX.](https://networkx.github.io)

* [Map drawing via Matplotlib.](https://matplotlib.org)

* [Data structures and type casting via NumPy.](http://www.numpy.org)

* [heapq-, operator-, itertools-, csv- and time-modules via Python Documentation.](https://docs.python.org/3/py-modindex.html)
