#Import the csv module
import csv

#Specify the file path
csvpath = "Resources/election_data.csv"

#Open the csv
with open(csvpath, 'r') as csvfile:

    #Read the csv
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store and skip the header
    csvheader = next(csvreader)

    #Dictionary of unique candidates
    unique = {}

    #Loop through the csv
    for candidate in csvreader:

        #Store unique Candidates in a dictionary with 1 starting vote
        if candidate[2] not in unique:
            unique[str(candidate[2])] = 1
        
        #Add 1 to a Candidate's vote count each time their name re-appears in the csv
        elif candidate[2] in unique:
            unique[str(candidate[2])] = unique[str(candidate[2])] + 1

    #Print the
    for candidate,votes in unique.items():
        print(f"{candidate}: {votes}")
        