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
    for candidate in csvreader:
        unique[str(candidate[2])] = 0            

    #Print the dictionary
    for candidate,votes in unique.items():
        print(f"{candidate}: {votes}")
        