import csv
import numpy
import networkx as nx
from helpers import *
from visualize import *
from pseudo import *


def main():
    # read .csv-files with the csv_reader()-function
    stations_holland = csvReader('StationsHolland.csv')
    connections_holland = csvReader('ConnectiesHolland.csv')

    # initialize graph with package nx
    graph = nx.Graph()
    criticals = []
    non_criticals = []
    all_stations = []
    
    # add all stations and attributes to the graph as nodes
    # type value 0 is critical, type value 1 is non-critical
    for station in stations_holland:
        all_stations.append(station[0])
        if station[3]:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 0)
            criticals.append(station[0])
        else:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 1)
            non_criticals.append(station[0])
    
    # add all connections and attributes to the graph as edges
    # type value 0 is critical, type value 1 is non-critical
    for connection in connections_holland:
        if (connection[0] in criticals) or (connection[1] in criticals):
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 0)
        else:
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 1)

    came_from, cost_so_far = dijkstra_search(graph, 'Den Haag Centraal', 'Schiedam Centrum')
    
    # e_large is the 
    e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    print(len(e_large))    
    
    path, graph2 = reconstruct_path(graph, came_from, 'Den Haag Centraal', 'Schiedam Centrum')
    print(path)
    e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    print(len(e_large))
    
    came_from, cost_so_far = dijkstra_search(graph2, 'Den Haag Centraal', 'Schiedam Centrum')
    path = reconstruct_path(graph2, came_from, 'Den Haag Centraal', 'Schiedam Centrum')
    print(path)
    e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    print(len(e_large))
    
    e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]
    
    
    # plot the railway map with all it's attributes
    draw(graph, criticals, non_criticals)


# call the main-function
if __name__ == "__main__":
    main()