# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:52:43 2018

@author: Kevin
"""
#importing calendar from script
from timetable import Calendar, displayT
import re 
import sys

c = Calendar()
print("Welcome to MrAdvisor!")

filename = input('Enter the file name, extension included: ')
if filename == 'quit':   #Allow user to quit at any time
       sys.exit()

pattern = r'.csv$' #Check for csv files
match = re.search(pattern,filename) 
while match == None:
   filename = input('Enter a valid filename, e.g example.csv: ')
   if filename == 'quit': #Allow user to quit at any time
       sys.exit()
   match = re.search(pattern,filename)

month_number = int(input('Enter the month number: ')) #Accept month number for calendar display
if month_number == 'quit': #Allow user to quit at any time
       sys.exit()
while type(month_number) != int or month_number < 1 or month_number > 12:
   month_number = int(input('Please enter a valid month number: '))
   if month_number == 'quit': #Allow user to quit at any time
       sys.exit()

c.load(filename) #open file
file = c.fill(month_number)  #Use prioritisation algorithm to fill calendar
displayT(file, month_number) #Display final calendar after removing clashes in events
