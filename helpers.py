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
    reader_list = list(reader)
    array = numpy.array(reader_list).astype('string')
    return array
    
# define a class for trains
class Train:
    current_location = ''
    previous_location = ''
    traveled_time = 0
    
# update a train's attributes
def update_train(train_name, new_location, all_stations, graph):
    # check if it's the first station the train attends
    if train_name.current_location == '':
        train_name.current_location = new_location
    else:         
        # retrieve the station indexes
        cur_index = all_stations.index(train_name.current_location)
        new_index = all_stations.index(new_location)
        
        # compute the traveld time with edge attributes
        minutes = graph[all_stations[cur_index]][all_stations[new_index]]['weight']
        train_name.traveled_time += minutes.astype(numpy.int)
        
        # update the train's location attributes
        train_name.previous_location = train_name.current_location
        train_name.current_location = new_location