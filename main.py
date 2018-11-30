# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:52:43 2018

@author: Kevin
"""

from timetable import Calendar, displayT
import re
import sys

c = Calendar()
print("Welcome to MrAdvisor!")

#filename = input('Enter the file name, extension included: ')
#if filename == 'quit':
#       sys.exit()
#
#pattern = r'.csv$'
#match = re.search(pattern,filename)
#while match == None:
#   filename = input('Enter a valid filename, e.g example.csv: ')
#   if filename == 'quit':
#       sys.exit()
#   match = re.search(pattern,filename)
#
#month_number = input('Enter the month number: ')
#if month_number == 'quit':
#       sys.exit()
#while type(month_number) != int or month_number < 1 or month_number > 12:
#   month_number = int(input('Please enter a valid month number: '))
#   if month_number == 'quit':
#       sys.exit()

filename = 'sample_calendar.csv'
c.load(filename)
for i in range(1,13):
    file = c.fill(i)
    displayT(file, i)