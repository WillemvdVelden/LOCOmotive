import csv
import numpy
import networkx as nx
from main import *

try:
    import matplotlib.pyplot as plt
except:
    raise

# read csv file from directory for vertices
def csvReader(csv_name):
    reader = csv.reader(open(csv_name, 'rb'), delimiter = ',')
    lReader = list(reader)
    array = numpy.array(lReader).astype('string')
    return array

# plot the railway map with all it's attributes
def draw(graph, c, n):
	eLarge = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 'critical']
	eSmall = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 'non-critical']

	# positions for all nodes
	pos = nx.get_node_attributes(graph, 'pos')
    
    # edge labels
	edgeLabels = nx.get_edge_attributes(graph, 'weight')

	# nodes
	nx.draw_networkx_nodes(graph, pos, nodelist = c, node_color = 'r', node_size = 150, alpha = 0.8)
	nx.draw_networkx_nodes(graph, pos, nodelist = n, node_color = 'b', node_size = 50, alpha = 0.8)

	# edges
	nx.draw_networkx_edges(graph, pos, edgelist = eLarge, width = 2)
	nx.draw_networkx_edges(graph, pos, edgelist = eSmall,
	                    width = 2, alpha = 0.5, edge_color = 'g', style = 'dashed')
	                    
	# labels
	nx.draw_networkx_labels(graph, pos, font_size = 8, font_family = 'sans-serif')
    
	nx.draw_networkx_edge_labels(graph, pos, edge_labels = edgeLabels, font_size = 8, font_family = 'sans-serif')
        
    # display
	plt.show()
    
# define a class for trains
class Train:
    currentLocation = ''
    previousLocation = ''
    traveledTime = 0
    
# update a train's attributes
def updateTrain(trainName, newLocation, allStations, graph):
    # check if it's the first station the train attends
    if trainName.currentLocation == '':
        trainName.currentLocation = newLocation
    else:         
        # retrieve the station indexes
        curIndex = allStations.index(trainName.currentLocation)
        newIndex = allStations.index(newLocation)
        
        # compute the traveld time with edge attributes
        minutes = graph[allStations[curIndex]][allStations[newIndex]]['weight']
        trainName.traveledTime += minutes.astype(numpy.int)
        
        # update the train's location attributes
        trainName.previousLocation = trainName.currentLocation
        trainName.currentLocation = newLocation
    
    
    
    