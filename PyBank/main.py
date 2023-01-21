import csv
from pickletools import int4

import numpy as geek

count = 0

accum = 0
with open('Resources/budget_data.csv') as file:
    lines = file.readlines()
    
    lst =[]

    for line in lines[1:]:
        accum += int(line.strip().split(',')[1])
        count += 1
        lst.append(int(line.strip().split(',')[1]))
        print(line)

    max_check = list(lst)[0]

    for elem in lst:
        if elem > max_check:
            max_check = elem

print(accum)
print(count)    
print(count)
print(max_check)

