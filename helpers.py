import csv
import numpy

# read csv file from directory for vertices
def csv_reader(csv_name):
    reader = csv.reader(open(csv_name, 'rb'), delimiter = ',')
    x = list(reader)
    array = numpy.array(x).astype("string")
    return array