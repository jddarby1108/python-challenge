import os

import csv

from collections import Counter

csv_path = os.path.join('Resources', 'budget_data.csv')

contents = []
dates = []
pl = []

#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    
    # append create lists and start formulas
    for row in csv_reader:
        dates.append(row[0])
        pl.append(float(row[1]))

        date_count = len(list(dates))
        pl_total = sum(pl)
        pl_avg = pl_total / date_count
        pl_max = max(pl)
        pl_min = min(pl)

print(date_count)
print(pl_total)
print(pl_avg)
print(pl_max)
print(pl_min)


#    The total number of months included in the dataset
#     date_count = len(list(csv_reader))
#     print(date_count)

# #    The net total amount of "Profit/Losses" over the entire period
#     for dates in enumerate(csv_reader):
#         print(dates)



# The average of the changes in "Profit/Losses" over the entire period
    # pl_sum = sum('Profit/Losses')
    # print(pl_sum)

# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period