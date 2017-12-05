# dijksta.py
# first algorithm
# finds a high value path from a starting station to a end station
# 
# heuristics team LOCOmotives
# team members: jasper, willem, mannus
#


import heapq
import numpy
import networkx as nx

# make a priority queue
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# Dijkstra's search algorithm
def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    current_time = {}
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph[current][next]['type']
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                #print(cost_so_far)
                priority = new_cost
                #print(priority)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

# get the correct path from Dijkstra's algorithm
def reconstruct_path(graph, came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    # set edge to non-critical

    # for i in range(len(path) - 1):
    #     graph[path[i]][path[i + 1]]['type'] = 1
    return path, graph
    
