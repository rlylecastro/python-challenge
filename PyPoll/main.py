#Import dependencies
import os
import csv

#Provide File Path
election = os.path.join('..', 'Resources', 'election_data.csv')

totalVotes = 0
candidateList = {}
winner = ''
mostVotes = 0

#Read in the csv file
with open(election, 'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile)
    #skip the header row
    header = next(csvreader)

    for row in csvreader:
        voterID = row[0]
        candidate = row[2]

        #Total number of votes cast
        totalVotes += 1
        #Populate candidateList with candidates
        if candidate not in candidateList:
            #The first time a new candidate is encountered, add it to the list with a vote count of 1
            candidateList[candidate] = 1
        else:
            #Each additional time the candidate is encountered, increment their vote count
            candidateList[candidate] += 1

    #Iterate over the candidates to determine the winner
    for candidate in candidateList:
        if candidateList[candidate] > mostVotes:
            mostVotes = candidateList[candidate]
            winner = candidate

outputText = f"""Election Results 
----------------------------
Total Votes: {totalVotes} 
----------------------------"""
for candidate in candidateList:
    outputText += f"\n{candidate}: {round(candidateList[candidate] / totalVotes * 100, 3)}% ({candidateList[candidate]})"
outputText += f"""\n----------------------------
Winner: {winner}
----------------------------"""

#Print the analysis to the terminal...    
print(outputText)    
    
#...and export to a text file with the results
outputFile = os.path.join('..', 'analysis', 'PyPollOutput.txt')
with open(outputFile, 'w') as datafile:
    datafile.write(outputText)