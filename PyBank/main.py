import os

import csv
csv_path = os.path.join('Resources', 'budget_data.csv')


#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")


    # # Read through each row of the data
    for row in csv_reader:

        date = (row[0])
        profit_loss = (row[1])

        print(date)
        print(profit_loss)
        
    
        



    