import networkx as nx

try:
    import matplotlib.pyplot as plt
except:
    raise

# plot the railway map with all it's attributes
# type value 1 is critical, type value 0 is non-critical
def draw_routes(graph, criticals, non_criticals, train_counter, max_trains):  
    
    routes = []
    
    for i in range(train_counter + 1):
        current = [(u, v) for (u, v, d) in graph.edges(data = True) if d['train'] == i]
        if (len(current) != 0):
            routes.append(current)

	# positions for all nodes
    pos = nx.get_node_attributes(graph, 'pos')
    
    # edge labels
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    # nodes
    nx.draw_networkx_nodes(graph, pos, nodelist = criticals, node_color = 'r', node_size = 150, alpha = 0.8)
    nx.draw_networkx_nodes(graph, pos, nodelist = non_criticals, node_color = 'b', node_size = 50, alpha = 0.8)
                    
    # 20 hex colors for possible train routes
    colors = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4',
            '#46f0f0', '#000080', '#f032e6', '#d2f53c', '#fabebe', '#008080', '#e6beff',
            '#aa6e28', '#800000', '#aaffc3', '#fffac8', '#808000', '#ffd8b1',
            '#808080', '#ff0000', '#00ff00']
            
    # routes
    for i in range(len(routes)):
        nx.draw_networkx_edges(graph, pos, edgelist = routes[i], width = 2, edge_color = colors[i])
                    
    # labels
    if (int(max_trains) == 7):
        nx.draw_networkx_labels(graph, pos, font_size = 8, font_family = 'sans-serif')

    nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_labels, font_size = 8, font_family = 'sans-serif')
    
    # display
    plt.show()