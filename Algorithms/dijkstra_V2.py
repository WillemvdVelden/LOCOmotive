# dijkstra_V2.py
# 
# Finds a high value path from a starting station to an end station.
# Uses a heuristic for time constraints.
# 
# Heuristics team LOCOmotive
#
# Teammembers: Jasper Naberman, Mannus Scomaker, Willem van der Velden

import heapq
import numpy

# initialize a priority queue
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# added heuristics for priority queue
def heuristic(new_cost, new_points, type, max_time):
    if new_cost > max_time:
        return 1000
    return -new_points

# looking through the graph
def Dijkstra_V2_search(graph, start, goal, max_time):
    # initialize variables
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    points_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    points_so_far[start] = 0 
    
    # start new step in path
    while not frontier.empty():
        current = frontier.get()
        
        # if goal is reached break out of loop
        if current == goal:
            break
        
        # check every neighbor of current node
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + int(graph[current][next]['weight'])
            new_points = points_so_far[current] + graph[current][next]['type']
            
            # check node only if it could be provitable 
            if next not in points_so_far or new_points < points_so_far[next]:
                cost_so_far[next] = new_cost
                points_so_far[next] = new_points
                priority = heuristic(new_cost, new_points, graph[current][next]['type'], max_time)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

# start reconstructing the best path using using the came_from dictionary
def reconstruct_Dijkstra_V2_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
