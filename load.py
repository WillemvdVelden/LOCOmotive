import csv
import numpy

# reader = csv.reader(open('ConnectiesHolland.csv', 'rb'), delimiter = ',')
# x = list(reader)
# ConnectiesHolland = numpy.array(x).astype("string")
# print ConnectiesHolland

# read csv file from directory
reader = csv.reader(open('StationsHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
StationsHolland = numpy.array(x).astype("string")

# ititiate new list with stations
station_list = []

# iterate over list and append station names to list
for lijst in StationsHolland:
	station_list.append(lijst[0])

print station_list