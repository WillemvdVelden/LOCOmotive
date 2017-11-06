
import csv
import numpy



class Graph(object):

    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

	def vertices(self):
		return list(self.__graph_dict.keys())

	def edges(self):
		return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
        	self.__graph_dict[vertex1].append(vertex2)
        	self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
    	edges = []
    	for vertex in self.__graph_dict:
    		for neighbour in self.__graph_dict[vertex]:
    			if {neighbour, vertex} not in edges:
    				edges.append({vertex, neighbour})
    			return edges

# intitialize graph
g = {}
graph = Graph(g)

# read csv file from directory for vertices
reader = csv.reader(open('StationsHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
StationsHolland = numpy.array(x).astype("string")

# iterate over list and append station names to list
for station in StationsHolland:
	graph.add_vertex(station[0])

# read csv file from directory for edges
reader = csv.reader(open('ConnectiesHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
ConnectiesHolland = numpy.array(x).astype("string")
for connectie in ConnectiesHolland:
	graph.add_edge({connectie[0], connectie[1]})

print(g)

