# main.py
# calls all functions and algoritems to solves the problem
# and compaires different solusoins
# 
# heuristics team LOCOmotives
# team members: jasper, willem, mannus
#

import csv
import numpy
import networkx as nx
import operator
import itertools
from Functions.helpers import *
from Functions.visualize import *
from Algorithms.dijkstra import *
from Algorithms.a_star import *

def main():
    # read .csv-files with the csv_reader()-function
    stations_holland = csvReader('datafiles/StationsHolland.csv')
    connections_holland = csvReader('datafiles/ConnectiesHolland.csv')

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
    
    best_path = []
    new_graph = graph
    counter = 0

    for i in range(7):
        counter = 0
        critical_counter = 0
        critical_counter2 = 0
        while True:
            station = all_stations[counter]
            counter += 1
            # for neighbor in graph.neighbors(station):
            #     if not graph[station][neighbor]['type']:
            #         counter += 1
            #         break
            # station = all_stations[counter]
            critical_counter = 0
            critical_counter2 = 0
            for station_to in all_stations:
                came_from, cost_so_far = A_search(new_graph, station, station_to)
                path = reconstruct_A_star_path(came_from, station, station_to)
                print(path)
                for i in range(len(path) - 1):
                    if new_graph[path[i]][path[i + 1]]['type'] == 1:
                        critical_counter2 += 1
                        
                if critical_counter < critical_counter2:
                     critcal_counter = critical_counter2
                     best_path.append(path)

            e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
            if (len(e_large) == 0 or counter == (len(all_stations) - 1)):
                break

        for i in range(len(best_path) - 1):
            if new_graph[path[i]][path[i + 1]]['type'] == 1:
                new_graph[path[i]][path[i + 1]]['type'] = 0

    # came_from, cost_so_far = A_search(graph, 'Zaandam', 'Zaandam')
    #
    # # the length of e_large is equal to the amount of critical connections
    # e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    # print(len(e_large))
    #
    # path = reconstruct_A_star_path(came_from, 'Zaandam', 'Zaandam')
    # print(path)
    # e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    # print(len(e_large))
    #
    # # came_from, cost_so_far = A_search(graph, 'Schiphol Airport', 'Zaandam')
    # # path = reconstruct_A_star_path(came_from, 'Schiphol Airport', 'Zaandam')
    # # print(path)
    # # e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    # # print(len(e_large))


    # plot the railway map with all it's attributes
    draw(graph, criticals, non_criticals)


# call the main-function
if __name__ == "__main__":
    main()
