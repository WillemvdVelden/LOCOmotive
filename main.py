import csv
import numpy
import networkx as nx
from helpers import *


def main():
    # read .csv-files with the csv_reader()-function
    StationsHolland = csvReader('StationsHolland.csv')
    ConnectionsHolland = csvReader('ConnectiesHolland.csv')

    # initialize graph with package nx
    graph = nx.Graph()
    c = []
    n = []
    allStations = []
    
    # add all stations and attributes to the graph as nodes
    for station in StationsHolland:
        allStations.append(station[0])
        if station[3]:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 'critical')
            c.append(station[0])
        else:
            graph.add_node(station[0], pos = (float(station[2]), float(station[1])), type = 'non-critical')
            n.append(station[0])
    
    # add all connections and attributes to the graph as edges
    for connection in ConnectionsHolland:
        if (connection[0] in c) or (connection[1] in c):
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 'critical')
        else:
            graph.add_edge(connection[0], connection[1], weight = connection[2], type = 'non-critical')
        
    # plot the railway map with all it's attributes
    draw(graph, c, n)
    
############## EXAMPLE #############    
    # initialize an object of class Train (see helpers.py)
    train1 = Train()
    
    # see how it looks like directly after creation
    print(train1.currentLocation, train1.previousLocation, train1.traveledTime)
    
    # let it start at centraal, go to amstel, and then to zuid (see helpers.py)
    updateTrain(train1, 'Amsterdam Centraal', allStations, graph)
    updateTrain(train1, 'Amsterdam Amstel', allStations, graph)
    updateTrain(train1, 'Amsterdam Zuid', allStations, graph)
    
    # see how it looks like now
    print(train1.currentLocation, train1.previousLocation, train1.traveledTime)
############## EXAMPLE END #############

# call the main-function
if __name__ == "__main__":
    main()