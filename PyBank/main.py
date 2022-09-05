import csv
from pickletools import int4

import numpy as geek

total_profit_losses = 0
current = 0
last = 0

total_change = 0
months = 0


with open("Resources/budget_data.csv", 'r') as file:
    csvreader = csv.DictReader(file)

    count = 0
    for row in csvreader:
        count += 1

    print("Total Months: ", count)
    
    

with open("Resources/budget_data.csv", 'r') as file:
    csvreader = csv.DictReader(file)

    profit_loss = sum(int(r['Profit/Losses']) for r in csvreader)

with open("Resources/budget_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    
   
    
    for row in csvreader:
        

        total_profit_losses = total_profit_losses + int(row[1])

        months = months + 1
        
        
        current = int(row[1])
        

        if months > 1:
            change = current - last

            total_change = total_change + change

            last = int(row[1])


            average_change = total_change / (months - 1) 

            

            

    
    # total1=0
    
    # for i in csvreader:
    #     total1 += 1
    #     print(int(i[1]))

    # print(f'Total: ${profit_loss }')

    # difference = count-profit_loss

    # average_loss = difference/profit_loss-count *100



    # print(average_loss)






#     sum = 0
        
#     for row in csvreader:
#         sum += csvreader
#     print(sum)

 
#     row_count = sum(1  for row in csvreader)

#     print(row_count)
#     next(csvreader)
#     for row in csvreader:
#         handle parsed row

# loop through all of the rows in the csv
#     for row in csvreader:
#         Date = (row["Date"])

#         print(len(Date))
        
#         total_profit_losses = total_profit_losses + int(row[1])

        


#   months = months + 1

#   current = int(row[1])

#   if months > 1:
#     change = current - last

#     total_change = total_change + change

#   last = int(row[1])


#   average_change = total_change