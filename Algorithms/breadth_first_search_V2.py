# breadth_first_search_V2.py
# 
# Breadth first search is an algorithm for searching graph data structures.
# 
# Heuristics team LOCOmotive
#
# Teammembers: Jasper Naberman, Mannus Scomaker, Willem van der Velden

import collections
import numpy

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()



def breadth_first_search_V2(graph, start):
    max_points = 0
    goal = ""
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    cost_so_far = {}
    points_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    points_so_far[start] = 0 

    counter = 0
    
    while not frontier.empty():
        current = frontier.get()
        counter += 1

        if cost_so_far[current] > 120:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph[current][next]['weight'].astype(numpy.int)
            if next not in came_from:
                new_points = points_so_far[current] + graph[current][next]['type']
            if new_points >= max_points:
                    max_points = new_points
            if next != current:
                cost_so_far[next] = new_cost
                points_so_far[next] = new_points
                frontier.put(next)
                came_from[next] = current
                goal = current
                
    return came_from, goal     

# get the correct path from Dijkstra's algorithm
def reconstruct_path_bfs_V2(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    return path   
    
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