#Script to analyze the company Profit/Loss Data

#We are working with a csv file so we need to import the csv module
import csv

#Specify the location of the csv file we are trying to examine
file_path = "Resources/budget_data.csv"

#Create two empty lists into which we will store the csv data

#The "date" list will hold the Date column values from the csv
date = []

#The "pl" list will hold the Profit/Losses column values from the csv
pl = []

#Open the csv and store it in a new variable "csvfile"
with open(file_path) as csvfile:

    #Read the file with comma as delimiter and store it in a new variable "csvreader"
    csvreader = csv.reader(csvfile, delimiter=',')

    #For each row in the variable "csvreader", print it to the terminal
    #for row in csvreader:
        #print(row)

    #Use the "next" function on "csvreader" to store the header in a new variable "csv_header"
    #This step lets us skip the header for all subsequent data analysis
    csv_header = next(csvreader)

    #Print the header
    #print(f"CSV Header: {csv_header}")

    #Example:
    #row1: 0,1
    #row2: 0,1
    #Loop through each row of data in the csv file we just read
    #For each row in the loop
    for row in csvreader:

        #Print the first index (index 0) to the Date list
        date.append(row[0])

        #Print the second index (index 1) to the Profit/Losses list
        pl.append(row[1])
    
    #Print how many months are in the Date list
    print(f"Total Months: {len(date)}")

#Create a variable to store the sum of the items in the Profit/Losses list
total = 0

#Loop through each index in the Profit/Losses list
#For each index in the loop
for cabbage in range(0, len(pl)):

    #Convert the value in that index to an integer
    #Add that integer to the current "total" variable
    #Overwrite the current "total" with this sum
    total = total + int(pl[cabbage])

#Print the total sum of the values in the Profit/Losses list
print(f"Total: ${total}")

    #Print the list of Dates
    #print(date)

    #Print the list of Profit/Losses
    #print(pl)

#Create a variable to store the sum of the differences from the Profit/Losses list
diftotal = 0

#Create a variable to store how many times we calculated a difference
numdiff = 0

#Loop through each index in the Profit/Losses list, starting with the second index
#For each index in the loop
for cabbage in range(1,len(pl)):

    #Convert the value in the index and the value in the previous index into integers
    #Find the difference between the value in the index and the value in the previous index
    #Store that difference in a new variable "diff"
    #Add that difference to the diftotal variable
    #Overwrite the currently stored diftotal with this sum
    diff = (int(pl[cabbage])-int(pl[cabbage-1]))
    diftotal = diftotal + diff

    #Add one to the number of differences we calculated
    numdiff = numdiff + 1

#Print the sum of the differences
print(diftotal)

#Print the number of differences we calculated
print(numdiff)

#Calculate the average change rounded to two decimals
#Store the average change in a new variable "avgchng"
avgchng = round(diftotal/numdiff, 2)

#Print the average change
print(f"Average change: ${avgchng}")


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