# simulated_annealing.py
# 
# Uses a hillclimber algorithm but sometimes accepts setbacks to possibly come
# to a better solution.
# 
# Heuristics team LOCOmotive
#
# Teammembers: Jasper Naberman, Mannus Scomaker, Willem van der Velden

from main import *

def sim_ann(path):
    y = []
    critical_start = 0
    
    # retrieve the amonount of critical connections in a path
    for i in range(len(path) - 1):
        critical_start += int(graph[path[i]][path[i + 1]]['type'])
        
    # set parameters for simulated annealing 
    old_cost = critical_start
    T = 1.0
    T_min = 0.01
    alpha = 1.0
    inters = 0
    y = []

    # ceep searching untill minimum temp has been reached 
    while T > T_min:
        inters += 1

        for i in range(10):
            # use hillclimber to compute a path
            path = hillclimber(graph, path, 10)
            
            
            # calculate the new paths value
            critical_start_new = 0
            for i in range(len(path) - 1):
                critical_start_new += int(graph[path[i]][path[i + 1]]['type'])
           
            # calculate the chance of accepting nieuw path
            new_cost = critical_start_new
            ap = numpy.exp((new_cost - old_cost) / T)
            
            # saveing new path as best path
            if old_cost < new_cost:
                solution = path
                old_cost = new_cost
            elif ap > random.random():
                solution = path
                old_cost = new_cost
            
        # calculating nieuw temprature
        T = alpha - (inters * ((alpha - T_min) / 1000))
   
    
    return solution
