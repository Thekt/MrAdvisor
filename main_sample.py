# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 00:02:45 2018

@author: Kevin
"""
from timetable import Calendar, displayT
import re
import sys

c = Calendar()
print("Welcome to MrAdvisor!")
filename = input('Enter the file name, extension included: ')
if filename == 'quit':
       sys.exit()

pattern = r'.csv$'
match = re.search(pattern,filename)
while match == None:
   filename = input('Enter a valid filename, e.g example.csv: ')
   if filename == 'quit':
       sys.exit()
   match = re.search(pattern,filename)
c.load(filename)
for i in range(1,13):
    file = c.fill(i)
    displayT(file, i)