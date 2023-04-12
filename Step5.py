import csv
import matplotlib.pyplot as plt


with open('data.csv') as data:

    sold = list(csv.reader(data))

sal21 = [int(sale) for sale in sold[-2][1:7]]
sal22 = [int(sale) for sale in sold[-1][1:7]]

sum21 = sum(sal21)
sum22 = sum(sal22)

sgr = (sum22 - sum21) / sum22

lastqtr21 = [int(sale) for sale in sold[-2][-6:]]
est22 = [lastqtr21[i] + (lastqtr21[i] * sgr) for i in range(6)]


plt.barh(range(6), est22, color='blue')
plt.yticks(range(6), ['July', 'August', 'September', 'October', 'November', 'December'])
plt.title('Estimated Sales for Last 6 Months of 2022')
plt.xlabel('Estimated Sales')
plt.ylabel('Month')
plt.show()
