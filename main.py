# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:52:43 2018

@author: Kevin
"""

from Calendar import Calendar
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

month_number = int(input('Enter the month number: '))
if month_number == 'quit':
       sys.exit()
while type(month_number) != int and month_number < 1 and month_number > 12:
   month_number = int(input('Please enter a valid month number: '))
   if month_number == 'quit':
       sys.exit()

# filename = 'calendar2.csv'
# month_number = 11
c.load(filename)
file = c.fill(month_number)
displayT(file, month_number)