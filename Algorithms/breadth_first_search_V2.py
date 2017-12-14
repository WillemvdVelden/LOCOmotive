# bfs.py
# third algorithm
# greedy breadth first search is an algorithm for searching graph data 
# structures.
# 
# heuristics team LOCOmotives
# team members: jasper, willem, mannus
#

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