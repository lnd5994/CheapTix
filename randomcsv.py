import random

with open('information.csv','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('info2.csv','w') as target:
    for _, line in data:
        target.write( line )