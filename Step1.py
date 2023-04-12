import csv

data = open('data.csv', 'r')

database = csv.reader(data)

for x in database:
    print(x)

data.close()
