import heapq
import numpy

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]



def heuristic(new_cost, new_points, type):
    if new_cost > 120:
        return 1000

    # if type == 0:
    #     return 20
    return (- new_points) 

# OSPF
def A_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    points_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    points_so_far[start] = 0 

    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph[current][next]['weight'].astype(numpy.int)
            new_points = points_so_far[current] + graph[current][next]['type']
            # print(current, next, new_points,heuristic(new_cost, new_points, graph[current][next]['type']))
            
            if next not in points_so_far or new_points < points_so_far[next]:
                cost_so_far[next] = new_cost
                points_so_far[next] = new_points
                priority = heuristic(new_cost, new_points, graph[current][next]['type'])
                # print(priority)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def reconstruct_A_star_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path