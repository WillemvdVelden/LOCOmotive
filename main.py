# main.py
#
# calls all functions and algorithms to solves the problem
# and compaires different solutions
# 
# Heuristics team LOCOmotive
# Team members: Jasper, Willem, Mannus
#

import csv
import numpy
import networkx as nx
import operator
import itertools
import time
import sys
from Functions.helpers import *
from Functions.visualize import *
from Algorithms.dijkstra import *
from Algorithms.dijkstra_V2 import *
from Algorithms.breadth_first_search import *
from Algorithms.breadth_first_search_V2 import *

def main():
    # initialize a starting clock to compute the running time of the main-function
    start = time.clock()
    
    # read .csv-files with the csv_reader()-function
    stations_holland = csv_reader('datafiles/StationsHolland.csv')
    connections_holland = csv_reader('datafiles/ConnectiesHolland.csv')

    # initialize graph with package nx
    graph = nx.Graph()
    criticals = []
    non_criticals = []
    all_stations = []
    
    # add all stations and attributes to the graph as nodes
    # type value 1 is critical, type value 0 is non-critical
    for station in stations_holland:
        all_stations.append(station[0])
        if station[3]:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 1)
            criticals.append(station[0])
        else:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 0)
            non_criticals.append(station[0])
    
    # add all connections and attributes to the graph as edges
    # type value 1 is critical, type value 0 is non-critical
    for connection in connections_holland:
        if (connection[0] in criticals) or (connection[1] in criticals):
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 1)
        else:
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 0)
    
    print()
    print("For Dijkstra's algorithm Version 2, type: 0")
    print("For a breadth first search algorithm, type: 1")
    print("For a breadth first search algorithm Version 2, type: 2")
    print()
    algorithm_type = input("Algorithm: ")
    
    # calling algorithm-functions from helpers
    if (int(algorithm_type) == 0):
        Dijkstra_V2_function(graph, all_stations)
    elif (int(algorithm_type) == 1):
        bfs_function(graph, all_stations)
    elif (int(algorithm_type) == 2):
        bfs_V2_function(graph, all_stations)
    else:
        print()
        sys.exit("Please provide valid input.")
    
    # compute the running time of the main-function
    print("Time past: {}".format(compute_running_time(start)))

# call the 'main'-function
if __name__ == "__main__":
    main()