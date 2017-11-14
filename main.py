import csv
import numpy
import networkx as nx
from helpers import *
from visualize import *


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
    for station in stations_holland:
        all_stations.append(station[0])
        if station[3]:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 'critical')
            criticals.append(station[0])
        else:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 'non-critical')
            non_criticals.append(station[0])
    
    # add all connections and attributes to the graph as edges
    for connection in connections_holland:
        if (connection[0] in criticals) or (connection[1] in criticals):
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 'critical')
        else:
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 'non-critical')
        
    # plot the railway map with all it's attributes
    draw(graph, criticals, non_criticals)
    
############## EXAMPLE #############    
    # initialize an object of class Train (see helpers.py)
    train_1 = Train()
    
    # see how it looks like directly after creation
    print(train_1.current_location, train_1.previous_location, train_1.traveled_time)
    
    # let it start at centraal, go to amstel, and then to zuid (see helpers.py)
    update_train(train_1, 'Amsterdam Centraal', all_stations, graph)
    update_train(train_1, 'Amsterdam Amstel', all_stations, graph)
    update_train(train_1, 'Amsterdam Zuid', all_stations, graph)
    
    # see how it looks like now
    print(train_1.current_location, train_1.previous_location, train_1.traveled_time)
############## EXAMPLE END #############

# call the main-function
if __name__ == "__main__":
    main()