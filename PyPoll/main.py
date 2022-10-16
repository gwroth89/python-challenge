# add modules
import csv
import os

# set file path and related variables
csvPath = os.path.join("..", "PyPoll", "resources", "election_data.csv")
electionData = open(csvPath)
csvReader = csv.reader(electionData, delimiter = ",")