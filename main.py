import csv
import numpy
import networkx as nx
from helpers import *
from graph import *

try:
    import matplotlib.pyplot as plt
except:
    raise

def main():
    # intitialize graph
    g = {}
    graph = Graph(g)

    # read csv file with csv_reader from helpers.py
    StationsHolland = csv_reader('StationsHolland.csv')

    # iterate over list and append station names to list
    for station in StationsHolland:
    	graph.add_station(station[0])

    # read csv file with csv_reader from helpers.py
    ConnectionsHolland = csv_reader('ConnectiesHolland.csv')

    # iterate over list and append connections to list
    for connection in ConnectionsHolland:
    	graph.add_connection({connection[0], connection[1]})

    # make new graph with package nx
    G = nx.Graph()
    
    for station in StationsHolland:
    	G.add_node(station[0])
        
    for connection in ConnectionsHolland:
    	G.add_edge(connection[0], connection[1], weight = connection[2])
        
    elarge=[(u,v) for (u,v,d) in G.edges(data = True) if d['weight'] > 0.5]
    esmall=[(u,v) for (u,v,d) in G.edges(data = True) if d['weight'] <= 0.5]
    
    # positions for all nodes
    pos = nx.spring_layout(G)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size = 100)
    
    # edges
    nx.draw_networkx_edges(G, pos, edgelist = elarge,
                        width = 2)
    nx.draw_networkx_edges(G,pos,edgelist = esmall,
                        width = 2,alpha = 0.5,edge_color = 'b',style = 'dashed')
                        
    # labels
    nx.draw_networkx_labels(G, pos, font_size = 8, font_family = 'sans-serif')
    
    # display
    plt.show()
    

# call the main-function
if __name__ == "__main__":
    main()