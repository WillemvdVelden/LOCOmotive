# dijksta.py
# first algorithm
# finds a high value path from a starting station to a end station
# 
# heuristics team LOCOmotives
# team members: jasper, willem, mannus
#

# prune_sorting.py
# 
# Starts Dijkstra V2 algorithm at a path with only one (critical) connection.
# 
# Heuristics team LOCOmotive
#
# Teammembers: Jasper Naberman, Mannus Scomaker, Willem van der Velden

import numpy
import networkx as nx

from Algorithms.dijkstra_V2 import *

# a pruning algorithm for sorting Dijkstra V2's order
def pruning_outside(graph, all_stations, max_time):
    new_graph = graph
    prune_stations =[]
    critical_counter = 0
    time_used = 0
    best_prune_paths = []
    best_prune = []
    
    # check which stations have 1 neighbour, that's also critical
    for station in all_stations:
        neighbors_count = 0
        neighbors_count_critical = 0
        for next in graph.neighbors(station):
            neighbors_count += 1
            if new_graph[next][station]['type'] == 1:
                neighbors_count_critical += 1
        if neighbors_count == 1 and neighbors_count_critical == 1:
            prune_stations.append(station)
    
    # use Dijkstra V2 to arrange a path from these stations first
    for station in prune_stations:
        for station_to in all_stations:
            critical_counter_2 = 0
            came_from, cost_so_far = Dijkstra_V2_search(new_graph, station, station_to, max_time)
            path = reconstruct_Dijkstra_V2_path(came_from, station, station_to)
            
            path_weight = 0
            for i in range(len(path) - 1):
                        path_weight += int(new_graph[path[i]][path[i + 1]]['weight'])
                        if new_graph[path[i]][path[i + 1]]['type'] == 1:
                            critical_counter_2 += 1
                    
            if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
                best_path_weight = path_weight
                critical_counter = critical_counter_2
                best_prune = path
                
        best_prune_paths.append(best_prune)
        time_used += best_path_weight
    
    # set the taken path to non-critical    
    for best_path in best_prune_paths:
        for i in range(len(best_path) - 1):
            if new_graph[best_path[i]][best_path[i + 1]]['type'] == 1:
                new_graph[best_path[i]][best_path[i + 1]]['type'] = 0
                    
    return new_graph, len(prune_stations), time_used
    