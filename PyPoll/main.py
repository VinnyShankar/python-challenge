#Start by importing the csv module
import csv

#specify the filepath
filepath = "Resources/election_data.csv"

candidates = []

#Open the csv
with open(filepath) as csvfile:

    #Read the csv
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header
    csvheader = next(csvreader)

    #Print the header (test)
    print(csvheader)

    #Loop through each row of the open csv file
    #For each row in the open csv file
    for row in csvreader:

        #Add the candidate to the list of candidates
        candidates.append(row[2])
    
    print(f"{len(candidates)}")

    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in candidates:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print(x)

election_analysis = ("Election results"
"\n-------------------------"
f"\nTotal Votes: {len(candidates)}"
"\n-------------------------"
)

print(election_analysis)


#Count the total number of votes (just like number of months from the budget csv)

#Count the unique strings in column three (expecting 3 unique candidates)
#Python has a embedded function called unique (ask Ahmad if we can use this)

#Count the number of times a candidate's name shows up
#Count the number of times a candidate's name shows up in the csv and divide by the total number of votes

#Max of the percentages and the name of the candidate with the highest percentage

#Print the analysis to the terminal and to a separate text file