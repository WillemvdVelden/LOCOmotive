import networkx as nx

try:
    import matplotlib.pyplot as plt
except:
    raise

# plot the railway map with all it's attributes
# type value 1 is critical, type value 0 is non-critical
def draw(graph, criticals, non_criticals):
	e_large = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 1]
	e_small = [(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 0]

	# positions for all nodes
	pos = nx.get_node_attributes(graph, 'pos')
    
    # edge labels
	edge_labels = nx.get_edge_attributes(graph, 'weight')

	# nodes
	nx.draw_networkx_nodes(graph, pos, nodelist = criticals, node_color = 'r', node_size = 150, alpha = 0.8)
	nx.draw_networkx_nodes(graph, pos, nodelist = non_criticals, node_color = 'b', node_size = 50, alpha = 0.8)

	# edges
	nx.draw_networkx_edges(graph, pos, edgelist = e_large, width = 2)
	nx.draw_networkx_edges(graph, pos, edgelist = e_small,
	                    width = 2, alpha = 0.5, edge_color = 'g', style = 'dashed')
	                    
	# labels
	nx.draw_networkx_labels(graph, pos, font_size = 8, font_family = 'sans-serif')
    
	nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_labels, font_size = 8, font_family = 'sans-serif')
        
    # display
	plt.show()