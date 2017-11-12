import csv
import numpy
import networkx as nx
from helpers import *
from draw import *


def main():
    # read csv file with csv_reader from helpers.py
    StationsHolland = csv_reader('StationsHolland.csv')

    # read csv file with csv_reader from helpers.py
    ConnectionsHolland = csv_reader('ConnectiesHolland.csv')

    # initialize graph with package nx
    graph = nx.Graph()
    c = []
    n = []
    for station in StationsHolland:
        if station[3]:
            graph.add_node(station[0], pos = (float(station[1]),float(station[2])), type = 'critical')
            c.append(station[0])
        else:
            graph.add_node(station[0], pos = (float(station[1]),float(station[2])) ,type = 'non-critical')
            n.append(station[0])

    print(c)
    print(graph)
    
    for connection in ConnectionsHolland:
        if (connection[0] in c) or (connection[1] in c):
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 'critical')
        else:
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 'non-critical')
        
    draw(graph, c, n)

    

# call the main-function
if __name__ == "__main__":
    main()