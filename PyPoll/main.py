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

    #Loop through the csv and store unique candidates in a dictionary
    for vote in csvreader:
        if vote[2] not in unique:
            unique[str(vote[2])] = 0
    
    for candidate in unique:
        print(candidate)