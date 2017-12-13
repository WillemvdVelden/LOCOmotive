# gbfs.py
# third algorithm
# greedy breadth first search is an algorithm for searching graph data 
# structures.
# 
# heuristics team LOCOmotives
# team members: jasper, willem, mannus
#

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()


def breadth_first_search_3(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from        

# get the correct path from Dijkstra's algorithm
def reconstruct_path_bfs(came_from, start, goal):
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