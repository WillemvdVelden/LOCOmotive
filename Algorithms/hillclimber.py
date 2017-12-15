from main import *

def hillclimber(graph, path, iters):
    path_weight = 0
    critical_start = 0

    for i in range(len(path) - 1):
        path_weight += int(graph[path[i]][path[i + 1]]['weight'])
        critical_start += int(graph[path[i]][path[i + 1]]['type'])
    critical_counter = 0
    best_path_weight = 0
    y = []

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

            neighbors = []
            for next in new_graph.neighbors(test_path[- 1]):
                neighbors.append(next)
        
            next_neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
            
            added_weight = int(new_graph[test_path[- 1]][next_neighbor]['weight'])

            if (path_weight + added_weight) > 120:
                break
            path_weight += added_weight
            test_path.append(next_neighbor)

        critical_counter_2 = 0
        for i in range(len(test_path) - 1):
            if new_graph[test_path[i]][test_path[i + 1]]['type'] == 1:
                critical_counter_2 += 1
                new_graph[test_path[i]][test_path[i + 1]]['type'] = 0

        if critical_counter < critical_counter_2 or ((critical_counter_2 == critical_counter) and (best_path_weight > path_weight)):
            best_path_weight = path_weight
            critical_counter = critical_counter_2
            path = test_path

    return path
