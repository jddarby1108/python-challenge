import os

import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    reader = csv.DictReader(csvfile)
    for row in reader:
         print(row['Date'], row['Profit/Losses'])

    
        



    