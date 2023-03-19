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

    #Use the "next" function on "csvreader" to store the header in a new variable "csv_header"
    #This step lets us skip the header for all subsequent data analysis
    csv_header = next(csvreader)

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

#Create a variable to store the sum of the items in the Profit/Losses list
total = 0

#Loop through each index in the Profit/Losses list
#For each index in the loop
for cabbage in range(0, len(pl)):

    #Convert the value in that index to an integer
    #Add that integer to the current "total" variable
    #Overwrite the current "total" with this sum
    total = total + int(pl[cabbage])

#Create a variable to store the sum of the differences from the Profit/Losses list
diftotal = 0

#Create a variable to store how many times we calculated a difference
numdiff = 0

#Create a variable to store the greatest increase in profits (largest difference)
greatestincrease = 0

#Create a variable to store the month of the greatest increase in profits
greatestincreasemonth = 0

#Create a variable to store the greatest decrease in profits (smallest difference)
greatestdecrease = 0

#Create a variable to store the month of the greatest increase in profits
greatestdecreasemonth = 0

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

    #If the stored differnce is greater than the stored greatest increase in profits
    if diff > greatestincrease:

        #Overwrite the greatest increase in profits with the stored difference
        greatestincrease = diff

        #Overwrite the greatest increase month
        greatestincreasemonth = str(date[cabbage])
    
    #If the stored difference is smaller than the stored greatest decrease in profits
    elif diff < greatestdecrease:

        #Overwrite the greatest decrease in profits with the stored difference
        greatestdecrease = diff

        #Overwrite the greatest decrease month
        greatestdecreasemonth = str(date[cabbage])

    #Add one to the number of differences we calculated
    numdiff = numdiff + 1

#Calculate the average change rounded to two decimals
#Store the average change in a new variable "avgchng"
avgchng = round(diftotal/numdiff, 2)

#Print the summary header
print("Financial Analysis")
print("----------------------------")

#Print how many months are in the Date list
print(f"Total Months: {len(date)}")

#Print the total sum of the values in the Profit/Losses list
print(f"Total: ${total}")

#Print the average change
print(f"Average change: ${avgchng}")

#Print the greatest increase in profits month and value
print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})")

#Print the greatest decrease in profits month and value
print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})")