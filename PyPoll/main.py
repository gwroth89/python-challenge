# add modules
import csv
import os


# set file path and related variables
csvPath = os.path.join("..", "PyPoll", "resources", "election_data.csv")
electionData = open(csvPath)
csvReader = csv.reader(electionData, delimiter = ",")
totalVotes = 0

# reads csv file and skips header 
with open(csvPath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    headerreader = next(reader)
    # loop through csv and get total votes. store columns in lists.
    for row in reader:
        totalVotes += 1
        ballotId = row[0]
        county = row[1]
        candidate = row[2]

print(totalVotes)