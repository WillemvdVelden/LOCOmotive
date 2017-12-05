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

def compute_score(total_critical, leftover_criticals, t, min):
    p = 1 - leftover_criticals / total_critical
    score = p * 10000 - (t * 20 + min / 10000)
    print(score)
    