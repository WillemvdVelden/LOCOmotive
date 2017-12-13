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



def breadth_first_search_3(graph, start):
    maxpoints = 0
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
            # print(current)
            # print(next)
            new_cost = cost_so_far[current] + graph[current][next]['weight'].astype(numpy.int)
            if next not in came_from:
                new_points = points_so_far[current] + graph[current][next]['type']
            # print(new_points, end="")
            # print(" = cost")
            if new_points >= maxpoints:
                    maxpoints = new_points
                    goal = next 
            if next != current:
                cost_so_far[next] = new_cost
                points_so_far[next] = new_points
                frontier.put(next)
                came_from[next] = current
        # print(maxpoints, end="")
        # print(" = max")

    
    print(goal)
    return came_from, goal     

# get the correct path from Dijkstra's algorithm
def reconstruct_path_bfs(came_from, start, goal):
    # print(goal)
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
    return path   