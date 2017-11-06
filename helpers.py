import csv

# read csv file from directory for vertices
reader = csv.reader(open('StationsHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
StationsHolland = numpy.array(x).astype("string")

# iterate over list and append station names to list
for lijst in StationsHolland:
	graph.add_vertex(lijst[0])

# read csv file from directory for edges
reader = csv.reader(open('ConnectiesHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
ConnectiesHolland = numpy.array(x).astype("string")

# iterate over list and append connections
for lijst in ConnectiesHolland:
	graph.add_edge({lijst[0],lijst[1]})