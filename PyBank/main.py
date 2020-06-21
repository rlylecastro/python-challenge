#Import dependencies
import os
import csv

#Provide File Path
finance = os.path.join('..', 'Resources', 'budget_data.csv')

totalMonths = 0
totalProfitLoss = 0
meanDeltaProfitLoss = 0
maxProfit = 0
maxProfitMonth = ''
maxLoss = 0
MaxLossMonth = ''

#Read in the csv file
with open(finance, 'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile)
    #skip the header row
    header = next(csvreader)
  
    for row in csvreader:
        #count total number of months in dataset
        totalMonths = totalMonths + 1
        totalProfitLoss = totalProfitLoss + int(row[1])
        #Greatest increase in profit (date and amount) over entire period
        if int(row[1]) > maxProfit:
            maxProfit = int(row[1])
            maxProfitMonth = row[0]
        #Greatest decrease in losses (date and amound) over the entire period
        if int(row[1]) < maxLoss:
            maxLoss = int(row[1])
            maxLossMonth = row[0]
    #Average of changes in Profit/Loss
    meanDeltaProfitLoss = round(totalProfitLoss / totalMonths, 0)

outputText = f"""Financial Analysis 
----------------------------
Total Months: {totalMonths} 
Total: ${totalProfitLoss} 
Average Change: ${meanDeltaProfitLoss} 
Greatest Increase in Profits: {maxProfitMonth} ${maxProfit} 
Greatest Decrease in Profits: {maxLossMonth} ${maxLoss}"""

#Print the analysis to the terminal...    
print(outputText)    
    
#...and export to a text file with the results
outputFile = os.path.join('..', 'analysis', 'PyBankOutput.txt')
with open(outputFile, 'w') as datafile:
    datafile.write(outputText)