import csv
import numpy

reader = csv.reader(open('ConnectiesHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
ConnectiesHolland = numpy.array(x).astype("string")
print ConnectiesHolland

reader = csv.reader(open('StationsHolland.csv', 'rb'), delimiter = ',')
x = list(reader)
StationsHolland = numpy.array(x).astype("string")
print StationsHolland