# graph.py
# grapy structure
# creates a graph node structure from 2 csv files
# 
# heuristics team LOCOmotives
# team members: jasper, willem, mannus
#

class Graph(object):

    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

	def stations(self):
		return list(self.__graph_dict.keys())

	def connections(self):
		return self.__generate_connections()

    def add_station(self, station):
        if station not in self.__graph_dict:
            self.__graph_dict[station] = []

    def add_connection(self, connection):
        connection = set(connection)
        (station1, station2) = tuple(connection)
        if station1 in self.__graph_dict:
        	self.__graph_dict[station1].append(station2)
        	self.__graph_dict[station2].append(station1)
        else:
            self.__graph_dict[station1] = [station2]

    def __generate_connections(self):
    	connections = []
    	for station in self.__graph_dict:
    		for neighbour in self.__graph_dict[station]:
    			if {neighbour, station} not in connections:
    				connections.append({station, neighbour})
    			return edges
