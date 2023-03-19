#Script to analyze the company Profit/Loss Data

#We are working with a csv file so we need to import the csv module
import csv

#Specify the location of the csv file we are trying to examine
file_path = "Resources/budget_data.csv"

#Open the csv and store it in a new variable csvfile
with open(file_path) as csvfile:

    #Read the file with comma as delimiter and store it in a new variable csvreader
    csvreader = csv.reader(csvfile, delimiter=',')

    #For each row in the variable, print it to the terminal
    #for row in csvreader:
        #print(row)
#Skip the header row by using the 'next' function (skip this step if there is no header)
    csv_header = next(csvreader)

    #Print the header
    print(f"CSV Header: {csv_header}")

# Create two empty lists
# Read the csv and append the values in the empty list
# Count the number of indices in one of the lists

#Read the csv file
#Create a list using the second column (Profit/Loss list)
#Count the number of indices in the Profit/Loss list

#Create a dictionary with the headers as the keys

#Sum the objects in the Profit/List list

#Loop through the values and calculate the difference at each step of the loop

#Create a variable to track the greatest increase in p/l
#Create a variable to track the month with the greatest increase in p/l

#Create a variable to track the greatest decrease in p/l
#Create a variable to track the month with the greatest decrease in p/l

#Write the analysis to a file (use .txt or .md etc)

#Dictionary
#Key0: object, object, object
#Key1: object, object, object