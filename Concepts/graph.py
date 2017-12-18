# graph.py
# Graph structure
# Creates a graph node structure from 2 .csv-files
# 
# Heuristics team LOCOmotive
# Teammembers: Jasper Naberman, Mannus Scomaker, Willem van der Velden

class Graph(object):
    # initialize a dictionary
    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
    
    # function returns all stations (nodes)
	def stations(self):
		return list(self.__graph_dict.keys())

    # function returns all connections (edges)
	def connections(self):
		return self.__generate_connections()
    
    # function adds a station (node) to the graph
    def add_station(self, station):
        if station not in self.__graph_dict:
            self.__graph_dict[station] = []

    # function adds a connection (edge) to the graph
    def add_connection(self, connection):
        connection = set(connection)
        (station1, station2) = tuple(connection)
        if station1 in self.__graph_dict:
        	self.__graph_dict[station1].append(station2)
        	self.__graph_dict[station2].append(station1)
        else:
            self.__graph_dict[station1] = [station2]
    
    # function initializes all connections between stations
    def __generate_connections(self):
    	connections = []
    	for station in self.__graph_dict:
    		for neighbour in self.__graph_dict[station]:
    			if {neighbour, station} not in connections:
    				connections.append({station, neighbour})
    			return edges
