# add modules
import csv
import os

# set file path and related variables
csvPath = os.path.join("..", "PyPoll", "resources", "election_data.csv")
electionData = open(csvPath)
csvReader = csv.reader(electionData, delimiter = ",")
totalVotes = 0
candidate = []
candidateList = []
candidateVoteList = []
outputFile = "pollanalysis.txt"
chuckVotes = 0
dianaVotes = 0
rayVotes = 0

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
        # find and store unique list of candidates
        if candidate not in candidateList:
            candidateList.append(candidate)
        # tabulate vote counts and store
        chuckVotes = chuckVotes + candidate.count('Charles Casper Stockham')
        dianaVotes = dianaVotes + candidate.count('Diana DeGette')
        rayVotes = rayVotes + candidate.count('Raymon Anthony Doane')
        # calculate each candidates votes share
        chuckPercent = chuckVotes / totalVotes
        dianaPercent = dianaVotes / totalVotes
        rayPercent = rayVotes / totalVotes
        # # identify the winner
        # candidateVoteList = [chuckVotes, dianaVotes, rayVotes]
        # winnerVoteCount = max(candidateVoteList)


# store and format output
output = (
    f"Total Votes: {totalVotes}\n"
    f"Charles Casper Stockham - Votes: {chuckVotes} Vote %: {chuckPercent}\n"
    f"Diana DeGette - Votes: {dianaVotes} Vote %: {dianaPercent}\n"
    f"Raymon Anthony Doane - Votes: {rayVotes} Vote %: {rayPercent}\n"
    #f"Winner: {profitLossMin} {minMonth}\n"
)

# print to console and output to txt file
print(output)

# with open(outputFile, 'w') as txtFile:
#      txtFile.write(output)