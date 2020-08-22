import os

import csv

from collections import Counter

csv_path = os.path.join('Resources', 'election_data.csv')

voter_id = []
county = []
candidates = []
all = []

#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    
    # append create lists and start formulas
    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[1])
        all = zip("voter_id", "county", "candidates")

#export results to a text file
output_path = os.path.join("new.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and write to file new
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow([voter_id]) 
    
