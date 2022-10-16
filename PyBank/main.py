# add modules
import csv
import os
from statistics import mean

# set file path and related variables
csvPath = os.path.join("..", "PyBank", "resources", "budget_data.csv")
budgetData = open(csvPath)
csvReader = csv.reader(budgetData, delimiter = ",")
totalMonths = 1
totalNet = 0
profitLossDelta = []
month = []
outputFile = "budgetanalysis.txt"

# read csv file into dictionary and add column for monthly profit delta
with open(csvPath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    headerreader = next(reader)
    previousNet = next(reader)
    previousNet = int(previousNet[1])
    # loop through CSV and get total months. store columns in lists. Calculate net profit/loss
    for row in reader:
        totalMonths += 1
        date = row[0]
        profitLoss = int(row[1])
        totalNet = totalNet + profitLoss
        netChange = profitLoss - previousNet
        profitLossDelta.append(netChange)
        month.append(date)
        previousNet = profitLoss

# calculate Max, Min, Mean of profit/loss
profitLossMax = max(profitLossDelta)
profitLossMin = min(profitLossDelta)
profitLossAverage = mean(profitLossDelta)
# find the corresponding month to Max and Min values
maxIndex = profitLossDelta.index(profitLossMax)
maxMonth = month[maxIndex]
minIndex = profitLossDelta.index(profitLossMin)
minMonth = month[minIndex]

# store and format output
output = (
    f"Total Months: {totalMonths}\n"
    f"Total: {totalNet}\n"
    f"Average Change: {profitLossAverage}\n"
    f"Greatest Increase: {profitLossMax} {maxMonth}\n"
    f"Greatest Decrease: {profitLossMin} {minMonth}\n"
)

# print to console and output to txt file
print(output)

with open(outputFile, 'w') as txtFile:
     txtFile.write(output)