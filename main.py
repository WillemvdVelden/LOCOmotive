import csv
import numpy
import networkx as nx
from helpers import *
from draw import *


def main():
    # intitialize graph
    g = {}
    graph = Graph(g)

    # read csv file with csv_reader from helpers.py
    StationsHolland = csv_reader('StationsHolland.csv')

    # iterate over list and append station names to list
    for station in StationsHolland:
    	graph.add_station(station[0])

    # read csv file with csv_reader from helpers.py
    ConnectionsHolland = csv_reader('ConnectiesHolland.csv')

    # iterate over list and append connections to list
    for connection in ConnectionsHolland:
    	graph.add_connection({connection[0], connection[1]})

    # make new graph with package nx
    G = nx.Graph()
    k = []
    n = []
    for station in StationsHolland:
        if station[3]:
            G.add_node(station[0], pos = (float(station[1]),float(station[2])) ,type = 'Kritiek')
            k.append(station[0])
        else:
            G.add_node(station[0], pos = (float(station[1]),float(station[2])) ,type = 'not')
            n.append(station[0])

    print(k)
    print(g)
    
    for connection in ConnectionsHolland:
        if (connection[0] in k) or (connection[1] in k):
            G.add_edge(connection[0], connection[1], weight = connection[2], type = 'Kritiek')
        else:
            G.add_edge(connection[0], connection[1], weight = connection[2], type = 'not')
        
    draw(G, g, k, n)

    

# call the main-function
if __name__ == "__main__":
    main()