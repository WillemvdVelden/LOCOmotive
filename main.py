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
from Functions.visualize_routes import *
from Algorithms.dijkstra import *
from Algorithms.dijkstra_V2 import *
from Algorithms.breadth_first_search import *
from Algorithms.breadth_first_search_V2 import *
from Algorithms.prune_sorting import *

def main():
    # initialize a starting clock to compute the running time of the main-function
    start = time.clock()
    
    print()
    print("For a map of Noord-Holland and Zuid-Holland, type: 0")
    print("For a map of The Netherland as a whole, type: 1")
    print()
    map_type = input("Map: ")
    
    max_trains = 0
    max_time = 0
    
    print()
    print("For a map with default connection values, type: 0")
    print("For a map with only critical connections, type: 1")
    print()
    connection_type = input("Connection-type: ")
    
    # read .csv-files with the csv_reader-function
    if (int(map_type) == 0):
        stations_holland = csv_reader('datafiles/StationsHolland.csv', connection_type)
        connections_holland = csv_reader('datafiles/ConnectiesHolland.csv', connection_type)
        max_trains = 7
        max_time = 120
    elif (int(map_type) == 1):
        stations_holland = csv_reader('datafiles/StationsNationaal.csv', connection_type)
        connections_holland = csv_reader('datafiles/ConnectiesNationaal.csv', connection_type)
        max_trains = 20
        max_time = 180
    else:
        print()
        sys.exit("Please provide valid input.")
        
    print()
    print("For Dijkstra's algorithm, type: 0")
    print("For Dijkstra's algorithm Version 2, type: 1")
    print("For a breadth first search algorithm, type: 2")
    print("For a breadth first search algorithm Version 2, type: 3")
    print()
    algorithm_type = input("Algorithm: ")
    
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
            graph.add_edge(connection[0], connection[1], weight = connection[2].strip('.0'), type = 1, train = 0)
        else:
            graph.add_edge(connection[0], connection[1], weight = connection[2].strip('.0'), type = 0, train = 0)
            
    # load data compatible for Dijkstra's algorithm
    if (int(algorithm_type) == 0):
        # add all connections and attributes to the graph as edges
        # type value 0 is critical, type value 1 is non-critical
        for connection in connections_holland:
            if (connection[0] in criticals) or (connection[1] in criticals):
                graph[connection[0]][connection[1]]['type'] = 0
            else:
                graph[connection[0]][connection[1]]['type'] = 1
    
    # calling algorithm-functions from helpers
    # if (int(algorithm_type) == 0):
    if (int(algorithm_type) == 0):
        dijkstra_function(graph, all_stations, max_trains) 
    elif (int(algorithm_type) == 1):
        print()
        print("Do you wish to use a sorting algorithm before Dijkstra's algorithm Version 2?")
        print("If yes, type 'y'. If no, type 'n'.")
        print()
        pruning_type = input("Sorting algorithm: ")
        
        if (pruning_type in ('y', 'Y', 'yes', 'Yes', 'YES')):
            new_graph, prune_station_count, time_used = pruning_outside(graph, all_stations, max_time)
            new_graph = dijkstra_V2_function(new_graph, all_stations, max_trains, max_time, prune_station_count, time_used, criticals, non_criticals)
        elif (pruning_type in ('n', 'N', 'no', 'No', 'NO')):
            new_graph = dijkstra_V2_function(graph, all_stations, max_trains, max_time, 0, 0, criticals, non_criticals)
        else:
            print()
            sys.exit("Please provide valid input.")            
    elif (int(algorithm_type) == 2):
        bfs_function(graph, all_stations, max_trains, max_time)
    elif (int(algorithm_type) == 3):
        bfs_V2_function(graph, all_stations, max_trains, max_time)
    else:
        print()
        sys.exit("Please provide valid input.")
    
    # compute the running time of the main-function
    print("Time past: {}".format(compute_running_time(start)))
    

# call the 'main'-function
if __name__ == "__main__":
    main()