# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:32:45 2018

@author: Ashwin Ashok
"""

import csv

file="Batsman_vulnerability_to_bowler.csv"
with open(file,'r') as csvfile:
    lines=csv.reader(csvfile)
    data = list(lines)
    print(data[0])