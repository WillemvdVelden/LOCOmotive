import csv
import numpy
import networkx as nx
from helpers import *
from graph import *

try:
    import matplotlib.pyplot as plt
except:
    raise

def draw(graph, c, n):
	eLarge = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 'critical']
	eSmall = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 'non-critical']

	# positions for all nodes
	pos = nx.get_node_attributes(graph, 'pos')

	# nodes
	nx.draw_networkx_nodes(graph, pos, nodelist = c, node_color = 'r', node_size = 150, alpha = 0.8)

	nx.draw_networkx_nodes(graph, pos,
		nodelist = n,
		node_color = 'b',
		node_size = 50,
		alpha = 0.8)

	# edges
	nx.draw_networkx_edges(graph, pos, edgelist = eLarge, width = 2)
	nx.draw_networkx_edges(graph, pos, edgelist = eSmall,
	                    width = 2, alpha = 0.5, edge_color = 'g', style = 'dashed')
	                    
	# labels
	nx.draw_networkx_labels(graph, pos, font_size = 8, font_family = 'sans-serif')

	# display
	plt.show()