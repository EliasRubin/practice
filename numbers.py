#!/usr/bin/env python3
import csv

with open('file.txt') as csvf:
    cr = csv.reader(csvf, delimiter = ',')
    for row in cr:
        print(row)
        
