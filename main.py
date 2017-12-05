# main.py
#
# calls all functions and algorithms to solves the problem
# and compaires different solutions
# 
# heuristics team LOCOmotive
# team members: Jasper, Willem, Mannus
#

import csv
import numpy
import networkx as nx
import operator
import itertools
from Functions.helpers import *
from Functions.visualize import *
from Algorithms.dijkstra import *
from Algorithms.dijkstra_V2 import *

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
    
    new_graph = graph
    counter = 0
    critical_counter = 0
    neighbor_counter = 0
    best_path_weight = 0

    for i in range(7):
        counter = 0
        best_path = []
        critical_counter = 0
        e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
    
        while True: # not len(e_large) == 0 or not counter == (len(all_stations) - 2):
            e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations)):
                # print("len e_large is: {}".format(len(e_large)))
                # print("len all_stations - 1 is: {}".format(len(all_stations) - 1))
                # print("counter is: {}".format(int(counter)))
                break
                        
            station = all_stations[counter]            
            
            neighbor_counter = 0
            
            for neighbor in graph.neighbors(station):
                if graph[station][neighbor]['type'] == 1:
                    neighbor_counter += 1

            if neighbor_counter == 0:
                counter += 1
                if counter != len(all_stations) - 1:
                    break

                # print(neighbor_counter)
                # print(station)

            station = all_stations[counter]
            
            counter += 1
            
            for station_to in all_stations:
                critical_counter_2 = 0
                came_from, cost_so_far = Dijkstra_V2_search(new_graph, station, station_to)
                path = reconstruct_Dijkstra_V2_path(came_from, station, station_to)
                
                path_weight = 0
                
                for i in range(len(path) - 1):
                    path_weight += new_graph[path[i]][path[i + 1]]['weight'].astype(numpy.int)
                    if new_graph[path[i]][path[i + 1]]['type'] == 1:
                        critical_counter_2 += 1
                
                if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
                    best_path_weight = path_weight
                    critical_counter = critical_counter_2
                    best_path = path

            # e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
            #
            # if int(len(e_large)) == 0 or int(counter) == (len(all_stations) - 1):
            #     print("len e_large is: {}".format(len(e_large)))
            #     print("len all_stations - 1 is: {}".format(len(all_stations) - 1))
            #     print("counter is: {}".format(int(counter)))
            #     break

        print(best_path)
        # print(len(best_path))
        for i in range(len(best_path) - 1):
            # print(new_graph[best_path[i]][best_path[i + 1]]['weight'])
            if new_graph[best_path[i]][best_path[i + 1]]['type'] == 1:
                new_graph[best_path[i]][best_path[i + 1]]['type'] = 0

    # came_from, cost_so_far = Dijkstra_V2_search(graph, 'Zaandam', 'Zaandam')
    #
    # # the length of e_large is equal to the amount of critical connections
    # e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    # print(len(e_large))
    #
    # path = reconstruct_Dijkstra_V2_path(came_from, 'Zaandam', 'Zaandam')
    # print(path)
    #
    # e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    # print(len(e_large))
    #
    # came_from, cost_so_far = Dijkstra_V2_search(graph, 'Schiphol Airport', 'Zaandam')
    # path = reconstruct_Dijkstra_V2_path(came_from, 'Schiphol Airport', 'Zaandam')
    # print(path)
    # e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    # print(len(e_large))


    # plot the railway map with all it's attributes
    draw(graph, criticals, non_criticals)


# call the 'main'-function
if __name__ == "__main__":
    main()