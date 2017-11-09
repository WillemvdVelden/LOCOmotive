import csv
import numpy
import networkx as nx
from helpers import *
from graph import *

try:
    import matplotlib.pyplot as plt
except:
    raise

def draw(G, g, k, n):
	elarge=[(u,v) for (u,v,d) in G.edges(data = True) if d['type'] == 'Kritiek']
	esmall=[(u,v) for (u,v,d) in G.edges(data = True) if d['type'] == 'not']

	pos=nx.get_node_attributes(G,'pos')
	# positions for all nodes
	# nodes
	nx.draw_networkx_nodes(G,pos, nodelist=k, node_color='r', node_size=150, alpha=0.8)

	nx.draw_networkx_nodes(G,pos,
		nodelist=n,
		node_color='b',
		node_size=50,
		alpha=0.8)

	# edges
	nx.draw_networkx_edges(G, pos, edgelist = elarge,
	                    width = 2)
	nx.draw_networkx_edges(G,pos,edgelist = esmall,
	                    width = 2, alpha = 0.5 ,edge_color = 'g',style = 'dashed')
	                    
	# labels
	nx.draw_networkx_labels(G, pos, font_size = 8, font_family = 'sans-serif')

	# display
	plt.show()