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

    #Store the candidate results in the variable "results"
    results = ""
    for candidate,votes in unique.items():
        percentage = round(((votes/total)*100), 3)
        results = results + f"{candidate}: {percentage}% ({votes})\n"

    #Store the election analysis in a variable
    election_analysis = (f"Election Results"
    "\n-------------------------"
    f"\nTotal Votes: {total}"
    "\n-------------------------"
    f"\n{results}"
    "-------------------------"
    f"\nWinner: {winner}"
    "\n-------------------------"
    )

    #Print the election analysis to the terminal
    print(election_analysis)

    #Specify the location of the .txt file where we will print the results
    text_path = "analysis/results.txt"

    #Open the file in write  mode
    with open(text_path, 'w') as f:

        #Write the results in the file
        f.write(election_analysis)