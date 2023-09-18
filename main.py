# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:24:07 2023

@author: andre
"""
monthCounter = 0
netTotal = 0
averageTotal = 0
GrChampion = 0
LtChampion = 0

PreviousRevenue = 0
RevenueChange = 0
RevenueChangeList = []

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"Financial Analysis")
   
    for row in csvreader:
        RevenueChange = eval(row[1]) - PreviousRevenue
        PreviousRevenue = eval(row[1])
        RevenueChangeList.append(RevenueChange)
        
        
        if GrChampion < eval(row[1]) :
            GrChampion = eval(row[1])
            GreatText = row[0]
        if LtChampion > eval(row[1]) :
            LtChampion = eval(row[1])
            LeastText = row[0]
        
        netTotal += eval(row[1])
        
        monthCounter = monthCounter + 1
    runningTotal = 0
    for i in RevenueChangeList:
        runningTotal =+ i
     
    averageTotal = runningTotal/monthCounter 
    print("\n")
    print(f"Total Months: {monthCounter}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${averageTotal}")
    print(f"Greatest Increase in Profits: {GreatText} ({GrChampion})")
    print(f"Greatest Decrease in Profits: {LeastText} ({LtChampion})")
    print("\n")

  


csvpath2 = os.path.join('Resources', 'election_data.csv')
previousCanidate = ""
VoteCounter = 0 
Canidates = []
List2 = []
with open(csvpath2) as csvfile2:
    
    csvreader2 = csv.reader(csvfile2, delimiter=',')
    
    csv_header2 = next(csvreader2)
    
    print(f"Election Results")
    print("\n")
    
    for row2 in csvreader2:
        VoteCounter += 1
        Canidates.append(row2[2])
        List2.append(row2[2])
        
    Canidates = list(set(Canidates))
    Count1 = 0
    Count2 = 0
    Count3 = 0
    percent1 = 0
    percent2 = 0
    percent3 = 0

    for j in List2:
        
        if j == Canidates[0]:
            Count1 += 1
        if j == Canidates[1]:
            Count2 += 1
        if j == Canidates[2]:
            Count3 += 1
    percent1 = Count1/VoteCounter * 100
    percent2 = Count2/VoteCounter * 100
    percent3 = Count3/VoteCounter * 100
    percent1 = round(percent1, 3)
    percent2 = round(percent2, 3)
    percent3 = round(percent3, 3)
    
        
        

    
print(f"Total Votes: {VoteCounter}")
print("\n")
print(f"{Canidates[0]}: {percent1}% ({Count1}) ")
print(f"{Canidates[1]}: {percent2}% ({Count2})")
print(f"{Canidates[2]}: {percent3}% ({Count3})")
print("\n")
        
        
if (Count1 > Count2) & (Count1 > Count3):
    print(f"Winner: {Canidates[0]}")
elif(Count2 > Count1) & (Count2 > Count3):
    print(f"Winner: {Canidates[1]}")
elif(Count3 > Count1) & (Count3 > Count2):
    print(f"Winner: {Canidates[2]}")       
        
        
        
        
        
        
        