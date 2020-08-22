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


        #    The total number of months included in the dataset
        date_count = len(list(dates))
        
        # the total of the profits and losses
        pl_total = sum(pl)

        # the average of the profits and losses
        pl_avg = pl_total / date_count

        # the greatest increase in profits and losses
        pl_max = max(pl)

        # the greatest decrease in profits and losses
        pl_min = min(pl)

# print all values to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {date_count}")
print(f"Total: $%5d" % (int(pl_total)))
print(pl_avg)
print(pl_max)
print(pl_min)

#export results to a text file
