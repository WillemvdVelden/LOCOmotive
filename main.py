import csv
import numpy
from helpers import *
from graph import *

# intitialize graph
g = {}
graph = Graph(g)

# read csv file with csv_reader from helpers.py
StationsHolland = csv_reader('StationsHolland.csv')

# iterate over list and append station names to list
for station in StationsHolland:
	graph.add_vertex(station[0])

# read csv file with csv_reader from helpers.py
ConnectionsHolland = csv_reader('ConnectiesHolland.csv')

# iterate over list and append connections to list
for connection in ConnectionsHolland:
	graph.add_edge({connection[0], connection[1]})

# print the graph
print(g)

