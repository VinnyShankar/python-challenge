#Start by importing the csv module
import csv

#specify the filepath
filepath = "Resources/election_data.csv"

#Open the csv
with open(filepath) as csvfile:

    #Read the csv
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header
    csvheader = next(csvreader)

    print(csvheader)

#Count the total number of votes (just like number of months from the budget csv)

#Count the unique strings in column three (expecting 3 unique candidates)
#Python has a embedded function called unique (ask Ahmad if we can use this)

#Count the number of times a candidate's name shows up
#Count the number of times a candidate's name shows up in the csv and divide by the total number of votes

#Max of the percentages and the name of the candidate with the highest percentage

#Print the analysis to the terminal and to a separate text file