vehiclesales = {}

with open('data.csv', 'r') as data:

    next(data)

    for line in data:
        fields = line.strip().split(',')
        year = int(fields[0][:4])

        if year in vehiclesales:
            vehiclesales[year] += int(fields[2])
        else:
            vehiclesales[year] = int(fields[2])

with open('stats.txt', 'w') as data:
    for year in range(2012, 2022):
        data.write(f"Year {year}: {vehiclesales.get(year, 0)} vehicles sold\n")
