# helpers.py
#
# defines functions to be used in main.py
# consists of a csv-reader, a score-function
# and a function to compute the running time of main.py
# 
# Heuristics team LOCOmotive
# Team members: Jasper, Willem, Mannus
#

from main import *

try:
    import matplotlib.pyplot as plt
except:
    raise

# read csv file from directory for vertices
def csv_reader(csv_name, connection_type):
    reader = csv.reader(open(csv_name, 'r'), delimiter = ',')
    reader_list = list(reader)
    for station in reader_list:
        if (len(station) == 3):
            station.append('')
    # make all connections critical when provided with that request
    if (csv_name == 'datafiles/StationsHolland.csv' or csv_name == 'datafiles/StationsNationaal.csv'):
        if (int(connection_type) == 1):
            for station in reader_list:
                station[3] = 'Kritiek'
    array = numpy.array(reader_list).astype('str')
    return array

# computes the score using the percentage of addressed critical connections,
# the amount of trains used and the sum of minutes ridden by all trains
def compute_score(total_critical, leftover_criticals, t, min):
    p = 1 - leftover_criticals / total_critical
    # compute the score and round to three decimals
    score = round(p * 10000 - (t * 20 + min / 10000), 3)
    return score

# computes the running time of main.py given the starting time of the script
def compute_running_time(start):
    # round the computed time to three decimals
    return round(time.clock() - start, 3)
    
# function for the Dijkstra's algorithm
def dijkstra_function(graph, all_stations, max_trains):
    new_graph = graph
    counter = 0
    critical_counter = 0
    neighbor_counter = 0
    best_path_weight = 0
    train_counter = 0
    minute_counter = 0
    critical_connections = len([(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 1])
    
    for i in range(max_trains):
            counter = 0
            best_path = []
            critical_counter = 0
            e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 0]
    
            while True:           
            
                if int(len(e_large)) == 0 or int(counter) == (len(all_stations)):
                    break

                station = all_stations[counter]
            
                counter += 1
            
                for station_to in all_stations:
                    critical_counter_2 = 0
                    came_from, cost_so_far = came_from, cost_so_far = dijkstra_search(new_graph, station, station_to)
                    path = reconstruct_path(new_graph, came_from, station, station_to)
                
                    path_weight = 0
                    
                    for i in range(len(path) - 1):
                        path_weight += int(new_graph[path[i]][path[i + 1]]['weight'])
                        if new_graph[path[i]][path[i + 1]]['type'] == 0:
                            critical_counter_2 += 1

                        if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
                            best_path_weight = path_weight
                            critical_counter = critical_counter_2
                            best_path = path

                e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 0]
            
                if int(len(e_large)) == 0 or int(counter) == (len(all_stations) - 1):
                    break
        
            if len(best_path) != 0:
                for i in range(len(best_path) - 1):
                    minute_counter += int(new_graph[best_path[i]][best_path[i + 1]]['weight'])
                train_counter += 1
        
            for i in range(len(best_path) - 1):
                if new_graph[best_path[i]][best_path[i + 1]]['type'] == 0:
                    new_graph[best_path[i]][best_path[i + 1]]['type'] = 1
    
    print()
    print("Dijkstra's Algorithm")
    print()
    print("Trains used: {} out of {}.".format(train_counter, max_trains))
    print("Score: {} out of 10000.".format(compute_score(critical_connections, int(len(e_large)), train_counter, minute_counter)))   
    
# function for the Dijkstra V2 algorithm
def dijkstra_V2_function(graph, all_stations, max_trains, max_time, train_counter, minute_counter, criticals, non_criticals):
    new_graph = graph
    counter = 0
    critical_counter = 0
    neighbor_counter = 0
    best_path_weight = 0
    critical_connections = len([(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 1])

    for i in range(max_trains):
        counter = 0
        best_path = []
        critical_counter = 0
        e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
    
        while True:           
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations)):
                break

            station = all_stations[counter]
            
            counter += 1
            
            for station_to in all_stations:
                critical_counter_2 = 0
                came_from, cost_so_far = Dijkstra_V2_search(new_graph, station, station_to, max_time)
                path = reconstruct_Dijkstra_V2_path(came_from, station, station_to)
                
                path_weight = 0
                
                for i in range(len(path) - 1):
                    path_weight += int(new_graph[path[i]][path[i + 1]]['weight'])
                    if new_graph[path[i]][path[i + 1]]['type'] == 1:
                        critical_counter_2 += 1
                
                if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
                    best_path_weight = path_weight
                    critical_counter = critical_counter_2
                    best_path = path

            e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations) - 1):
                break
        
        if len(best_path) != 0:
            for i in range(len(best_path) - 1):
                minute_counter += int(new_graph[best_path[i]][best_path[i + 1]]['weight'])
            train_counter += 1
        
        for i in range(len(best_path) - 1):
            new_graph[best_path[i]][best_path[i + 1]]['train'] = train_counter
            if new_graph[best_path[i]][best_path[i + 1]]['type'] == 1:
                new_graph[best_path[i]][best_path[i + 1]]['type'] = 0 
                   
    print()
    print("Dijkstra's Algorithm Version 2")
    print()
    print("Trains used: {} out of {}.".format(train_counter, max_trains))
    print("Score: {} out of 10000.".format(compute_score(critical_connections, int(len(e_large)), train_counter, minute_counter)))
    draw_routes(graph, criticals, non_criticals, train_counter)
    return new_graph
    
# function for the breadth first search algorithm
def bfs_function(graph, all_stations, max_trains, minute_counter):
    new_graph = graph
    counter = 0
    critical_counter = 0
    neighbor_counter = 0
    best_path_weight = 0
    train_counter = 0
    critical_connections = len([(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 1])

    for i in range(max_trains):
        counter = 0
        best_path = []
        critical_counter = 0
        e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
    
        while True:          
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations)):
                break

            station = all_stations[counter]
            
            counter += 1
            
            for station_to in all_stations:
                critical_counter_2 = 0
                came_from = breadth_first_search(new_graph, station, station_to)
                path = reconstruct_path_bfs(came_from, station, station_to)
                
                path_weight = 0
                
                for i in range(len(path) - 1):
                    path_weight += int(new_graph[path[i]][path[i + 1]]['weight'])
                    if new_graph[path[i]][path[i + 1]]['type'] == 1:
                        critical_counter_2 += 1
                
                if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
                    best_path_weight = path_weight
                    critical_counter = critical_counter_2
                    best_path = path

            e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations) - 1):
                break
        
        if len(best_path) != 0:
            for i in range(len(best_path) - 1):
                minute_counter += int(new_graph[best_path[i]][best_path[i + 1]]['weight'])
            train_counter += 1
        
        for i in range(len(best_path) - 1):
            if new_graph[best_path[i]][best_path[i + 1]]['type'] == 1:
                new_graph[best_path[i]][best_path[i + 1]]['type'] = 0
    
    print()
    print("Breadth First Search")
    print()
    print("Trains used: {} out of {}.".format(train_counter, max_trains))
    print("Score: {} out of 10000.".format(compute_score(critical_connections, int(len(e_large)), train_counter, minute_counter)))
    
    
# function for the breadth first search algorithm
def bfs_V2_function(graph, all_stations, max_trains):
    new_graph = graph
    counter = 0
    critical_counter = 0
    neighbor_counter = 0
    best_path_weight = 0
    train_counter = 0
    minute_counter = 0
    critical_connections = len([(u, v) for (u, v, d) in graph.edges(data = True) if d['type'] == 1])

    for i in range(max_trains):
        counter = 0
        best_path = []
        critical_counter = 0
        e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
    
        while True:          
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations)):
                break

            station = all_stations[counter]
            
            counter += 1
            print("pat")
            critical_counter_2 = 0
            came_from, goal = breadth_first_search_V2(new_graph, station)
            print(1)
            path = reconstruct_path_bfs_V2(came_from, station, goal)
            
            path_weight = 0
            
            for i in range(len(path) - 1):
                path_weight += int(new_graph[path[i]][path[i + 1]]['weight'])
                if new_graph[path[i]][path[i + 1]]['type'] == 1:
                    critical_counter_2 += 1
            
            if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
                best_path_weight = path_weight
                critical_counter = critical_counter_2
                best_path = path

            e_large = [(u, v) for (u, v, d) in new_graph.edges(data = True) if d['type'] == 1]
            
            if int(len(e_large)) == 0 or int(counter) == (len(all_stations) - 1):
                break
        
        if len(best_path) != 0:
            for i in range(len(best_path) - 1):
                minute_counter += int(new_graph[best_path[i]][best_path[i + 1]]['weight'])
            train_counter += 1
        
        for i in range(len(best_path) - 1):
            if new_graph[best_path[i]][best_path[i + 1]]['type'] == 1:
                new_graph[best_path[i]][best_path[i + 1]]['type'] = 0
    
    print()
    print("Breadth First Search V2")
    print()
    print("Trains used: {} out of {}.".format(train_counter, max_trains))
    print("Score: {} out of 10000.".format(compute_score(critical_connections, int(len(e_large)), train_counter, minute_counter)))