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

    #Dictionary to store unique candidates and their vote counts
    unique = {}

    #Loop through the csv
    for candidate in csvreader:

        #Store unique candidates in a dictionary with 1 vote each
        if candidate[2] not in unique:
            unique[str(candidate[2])] = 1
        
        #Add 1 to a candidate's vote count each time their name re-appears in the csv
        elif candidate[2] in unique:
            unique[str(candidate[2])] = unique[str(candidate[2])] + 1
    
    #Calculate the total number of votes
    total = sum(unique.values())

    #Find the candidate with the most votes
    winner = max(unique, key=unique.get)

    #Print the election results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")
    for candidate,votes in unique.items():
        percentage = round(((votes/total)*100), 3)
        print(f"{candidate}: {percentage}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")