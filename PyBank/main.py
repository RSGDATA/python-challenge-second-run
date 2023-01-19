import csv
from pickletools import int4

import numpy as geek

count = 0

accum = 0
with open('Resources/budget_data.csv') as file:
    lines = file.readlines()

    for line in lines[1:]:
        accum += int(line.strip().split(',')[1])
        count += 1
        print(line)
print(accum)
print(count)    

print(accum/count)