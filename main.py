# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:24:07 2023

@author: andre
"""
'first set of code startup values'
monthCounter = 0
netTotal = 0
averageTotal = 0
GrChampion = 0
LtChampion = 0
PreviousRevenue = 0
RevenueChange = 0
'revenue change list is a dictionary'
RevenueChangeList = {}
LeastText = ""
GreatText = ""

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")

with open(csvpath) as csvfile:
    
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    first_row = next(csvreader)
    PreviousRevenue = int(first_row[1])
    netTotal += int(first_row[1])
    
    'creates a new list with only the change in revenue'
    for row in csvreader:
        
        
        RevenueChange = eval(row[1]) - PreviousRevenue
        PreviousRevenue = int(row[1])
        RevenueChangeList[RevenueChange] = row[0]
        netTotal += int(row[1])
        monthCounter = monthCounter + 1
    runningTotal = 0
    
    'looks for the greatest value and least value'
    for i in RevenueChangeList:
        
        if GrChampion < i :
            GrChampion = i
            GreatText = RevenueChangeList.get(i)
        if LtChampion > i :
            LtChampion = i
            LeastText = RevenueChangeList.get(i)
        
        runningTotal =+ i
    'grabs the average'
    averageTotal =sum(RevenueChangeList)/len(RevenueChangeList)
    
output = ( 
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {monthCounter}\n"
    f"Total: ${netTotal}\n"
    f"Average Change: ${averageTotal:.2f}\n"
    f"Greatest Increase in Profits: {GreatText} ({GrChampion})\n"
    f"Greatest Decrease in Profits: {LeastText} ({LtChampion})\n")

print(output)
 
# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
    
    
'PyPoll code start'


csvpath2 = os.path.join('Resources', 'election_data.csv')
file_to_output2 = os.path.join("analysis", "election_analysis.txt")


previousCanidate = ""
VoteCounter = 0 
Canidates = []
List2 = []


with open(csvpath2) as csvfile2:
    
    csvreader2 = csv.reader(csvfile2, delimiter=',')
    
    csv_header2 = next(csvreader2)
    
    
    'counts the total and sends to a new list'
    for row2 in csvreader2:
        VoteCounter += 1
        Canidates.append(row2[2])
        List2.append(row2[2])
    
    'turns the list into a set and then that removes all duplicates'
    Canidates = list(set(Canidates))
    
    
    Count1 = 0
    Count2 = 0
    Count3 = 0
    percent1 = 0
    percent2 = 0
    percent3 = 0
    
    'counts all the votes indivudually'
    for j in List2:
        
        if j == Canidates[0]:
            Count1 += 1
        if j == Canidates[1]:
            Count2 += 1
        if j == Canidates[2]:
            Count3 += 1
    'Stores all the values to be used in output'
    percent1 = Count1/VoteCounter * 100
    percent2 = Count2/VoteCounter * 100
    percent3 = Count3/VoteCounter * 100
    percent1 = round(percent1, 3)
    percent2 = round(percent2, 3)
    percent3 = round(percent3, 3)
    
        
output2 = (
    f"Election Results\n"
    f"--------------------\n"
    f"Total Votes: {VoteCounter}\n"
    f"--------------------\n"
    f"{Canidates[0]}: {percent1}% ({Count1})\n "
    f"{Canidates[1]}: {percent2}% ({Count2})\n"
    f"{Canidates[2]}: {percent3}% ({Count3})\n"
    f"--------------------\n")


'Compares who will be the winner and prints'
if(Count1 > Count2) & (Count1 > Count3):
    output3 = (f"Winner: {Canidates[0]}\n"
               f"--------------------\n")
elif(Count2 > Count1) & (Count2 > Count3):
    output3 = (f"Winner: {Canidates[1]}\n"
               f"--------------------\n")
elif(Count3 > Count1) & (Count3 > Count2):
    output3 = (f"Winner: {Canidates[2]}\n"
               f"--------------------\n")     
'outputs'      
print(output2 + output3)
 
# Export the results to text file
with open(file_to_output2, "w") as txt_file:
    txt_file.write(output2 + output3)
        
        
        
        
        
        