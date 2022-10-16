# add modules
import csv
import os

# set file path and related variables
csvPath = os.path.join("..", "PyBank", "resources", "budget_data.csv")
budgetData = open(csvPath)
csvReader = csv.reader(budgetData, delimiter = ",")
totalMonths = 0
totalNet = 0
profitLossDelta = 0

# read csv file into dictionary and add column for monthly profit delta
with open(csvPath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    headerreader = next(reader)
    #loop through CSV and get total months. store columns in lists. Calculate net profit/loss
    for row in reader:
        totalMonths += 1
        date = row[0]
        profitLoss = int(row[1])
        totalNet = totalNet + profitLoss
        profitLossDelta = (row[1] + 1) - row[1]
        #profitLossMax = max(profitLossDelta)
        #profitLossMin = min(profitLossDelta)
        
# print the results
print(totalMonths)
print(totalNet)
print(profitLossDelta)