# hillclimber.py
# 
# hillclimber algorithm that picks a random node, and makes a path
# from there by picking random neighbours.
# 
# Heuristics team LOCOmotive
#
# Teammembers: Jasper Naberman, Mannus Scomaker, Willem van der Velden

from main import *

# hillclimber algorithm
def hillclimber(graph, path, iters, max_time):
    path_weight = 0
    critical_start = 0
    
    # iterate over the given path
    for i in range(len(path) - 1):
        path_weight += int(graph[path[i]][path[i + 1]]['weight'])
        critical_start += int(graph[path[i]][path[i + 1]]['type'])
    critical_counter = 0
    best_path_weight = 0
    y = []
    
    # loop over as many iterations as inputted
    for i in range(iters):
        new_graph = copy.deepcopy(graph)
        path_weight = 0
        if len(path) <= 3:
            test_path = path[:random.randint(1, len(path))]
        else:
            test_path = path[:random.randint(1, len(path) -3)]
        for i in range(len(path) - 1):
            path_weight += int(new_graph[path[i]][path[i + 1]]['weight'])
            
        while True:
            # pick a random neighbour while the path stays under a certain amount of time
            neighbors = []
            for next in new_graph.neighbors(test_path[- 1]):
                neighbors.append(next)
        
            next_neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
            
            added_weight = int(new_graph[test_path[- 1]][next_neighbor]['weight'])

            if (path_weight + added_weight) > max_time:
                break
            path_weight += added_weight
            test_path.append(next_neighbor)

        critical_counter_2 = 0
        
        # set the taken path to non-critical and count the value of each path
        for i in range(len(test_path) - 1):
            if new_graph[test_path[i]][test_path[i + 1]]['type'] == 1:
                critical_counter_2 += 1
                new_graph[test_path[i]][test_path[i + 1]]['type'] = 0

        # if the new path is the best path so far save it
        if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
            best_path_weight = path_weight
            critical_counter = critical_counter_2
            path = test_path

    return path
