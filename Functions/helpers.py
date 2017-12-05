# helpers.py
#
# defines functions to be used in main.py
# consists of a csv-reader, a score-function
# and a function to compute the running time of main.py
# 
# Heuristics team LOCOmotive
# Team members: Jasper, Willem, Mannus
#

import csv
import numpy
import networkx as nx
from main import *

try:
    import matplotlib.pyplot as plt
except:
    raise

# read csv file from directory for vertices
def csv_reader(csv_name):
    reader = csv.reader(open(csv_name, 'r'), delimiter = ',')
    reader_list = list(reader)
    array = numpy.array(reader_list).astype('str')
    return array

# computes the score using the percentage of addressed critical connections,
# the amount of trains used and the sum of minutes ridden by all trains
def compute_score(total_critical, leftover_criticals, t, min):
    p = 1 - leftover_criticals / total_critical
    score = p * 10000 - (t * 20 + min / 10000)
    print(score)

# computes the running time of main.py given the starting time of the script
def compute_running_time(start):
    print(round(time.clock() - start, 3))