from main import *

def sim_ann(path):
    y = []
    critical_start = 0
    for i in range(len(path) - 1):
        critical_start += int(graph[path[i]][path[i + 1]]['type'])
        
    old_cost = critical_start
    T = 1.0
    T_min = 0.01
    alpha = 1.0
    inters = 0
    y = []

    while T > T_min:
        inters += 1

        for i in range(10):
            path = hilclimber(graph, path, 10)
            critical_start_new = 0
            for i in range(len(path) - 1):
                critical_start_new += int(graph[path[i]][path[i + 1]]['type'])
            new_cost = critical_start_new
            ap = numpy.exp((new_cost - old_cost) / T)
            if old_cost < new_cost:
                solution = path
                old_cost = new_cost
            elif ap > random.random():
                solution = path
                old_cost = new_cost
            y.append(old_cost)
        T = alpha - ( inters * ( (alpha - T_min) / 1000) )
    x = range(len(y))
    plt.plot(x,y)
    plt.show()
    
    return solution
