import csv
import matplotlib.pyplot as plt


sales = []
with open('data.csv', 'r') as record:
    reader = csv.reader(record)
    for row in reader:
        sales.append(row)


years = [int(row[0]) for row in sales[1:]]
totals = [sum(map(int, row[1:])) for row in sales[1:]]


plt.bar(years, totals)
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales by Year')
plt.show()
