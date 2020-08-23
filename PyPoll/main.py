import os

import csv


csv_path = os.path.join('Resources', 'election_data.csv')

voter_ids = []
counties = []
candidates = []
spacer = ("---------------------")
person = []
candidate_list = []
votes = []

#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    
    # append create lists and start formulas
    for row in csv_reader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
        
        #    The total number of votes cast
        vote_count = len(voter_ids)


    # find candidates
    person = set(candidates)
    y = len(person)

    
    for index, y in enumerate(person):


    # # loop through candidates for calculation
        if person == candidates:
            candidate_list.append(person[index], len(voter_ids))
               

         
            
    

    # def results:
    #     votes = len(voter_ids)

    

        

# print all values to the terminal
print("Election Results")
print(spacer)
print(f"Total Votes: {vote_count}")
print(spacer)
print(candidate_list)






#export results to a text file
output_path = os.path.join("new.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and write to file new
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"]) 
    csvwriter.writerow([spacer])
    csvwriter.writerow([f"Total Votes: %5d " % (int(vote_count))])
    csvwriter.writerow([spacer])

    
