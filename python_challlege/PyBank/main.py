import os
import csv

filename = os.path.join("Resources", "budget_data.csv")

with open (filename) as csvfile:
    
    csvreader =  csv.reader(csvfile, delimiter = ",")

    print(csvreader)

    csv_header = next(csvreader)
    
    print(f"csv header : {csv_header}")
    totalmonths = 0
    for row in csvreader:
        print(row)
        
        print(row [0])
        
        print(row [1])
        
        totalmonths = totalmonths + 1
        



with open (filename) as csvfile:
    
    csvreader = csv.reader(csvfile)
   
    next(csvreader)

    
    previous_profit_loss = 0
    changes = []
    
   
    for row in csvreader:
      
        profit_loss = int(row[1])
        
        
        change = profit_loss - previous_profit_loss
        
      
        changes.append(change)
        
        
        previous_profit_loss = profit_loss


average_change = sum(changes) / len(changes)

print(f"Average Change in Profit/Losses: ${average_change:.2f}")


with open (filename) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

   
    greatest_increase = 0
    greatest_increase_date = ""
    previous_profit_loss = 0
    
    
    for row in csvreader:
        
        profit_loss = int(row[1])
        date = row[0]
        
      
        change = profit_loss - previous_profit_loss
        
        
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date
        
        previous_profit_loss = profit_loss

print(f"Greatest Increase in Profits: ${greatest_increase} on {greatest_increase_date}")



with open (filename) as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)

    
    greatest_decrease = 0
    greatest_decrease_date = ""
    greatest_decrease_amount = 0
    previous_profit_loss = 0

    
    for row in csvreader:
       
        profit_loss = int(row[1])
        date = row[0]
        
        
        change = profit_loss - previous_profit_loss
        
       
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date
            greatest_decrease_amount = profit_loss
        
        
        previous_profit_loss = profit_loss

print(f"Greatest Decrease in Profits: ${greatest_decrease_amount} on {greatest_decrease_date}")
