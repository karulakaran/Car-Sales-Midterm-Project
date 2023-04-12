import csv

with open('data.csv') as file:

    contents = list(csv.reader(file))

sal21 = [int(sale) for sale in contents[-2][1:7]]
sal22 = [int(sale) for sale in contents[-1][1:7]]

sum21 = sum(sal21)
sum22 = sum(sal22)

sgr = (sum22 - sum21) / sum22

with open('stats.txt', 'a') as file:
    file.write(f"Sales Growth Rate: {sgr:.2f}\n")

lastqtr21 = [int(sale) for sale in contents[-2][-6:]]
est22 = [lastqtr21[i] + (lastqtr21[i] * sgr) for i in range(6)]

with open('stats.txt', 'a') as file:
    file.write("Estimated Sales for Last 6 Months of 2022:\n")
    for i in range(6):
        file.write(f"Month {i+7}: {est22[i]:.0f}\n")
