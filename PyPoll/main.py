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

    #Print the election results to the terminal
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

    #Specify the location of the .txt file where we will print the results
    text_path = "analysis/results.txt"

    #Open the file
    with open(text_path, 'w') as f:

        #Print the results
        f.write("Election Results")
        f.write("\n-------------------------")
        f.write(f"\nTotal Votes: {total}")
        f.write("\n-------------------------")
        for candidate,votes in unique.items():
            percentage = round(((votes/total)*100), 3)
            f.write(f"\n{candidate}: {percentage}% ({votes})")
        f.write("\n-------------------------")
        f.write(f"\nWinner: {winner}")
        f.write("\n-------------------------")
