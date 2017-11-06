import csv
import numpy
from helpers import *
from graph import *
import networkx as nx

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
    test = nx.Graph()
    
    for station in StationsHolland:
    	test.add_node(station[0])
        
    for connection in ConnectionsHolland:
    	test.add_edge(connection[0], connection[1])
    
        
    print test.nodes()
    print test.edges()
    
    

# call the main-function
if __name__ == "__main__":
    main()