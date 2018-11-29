# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:53:42 2018

@author: Kevin
"""
import csv

DICT_MONTHS = {
        1:{'month': 'January','days': 31,'code': 'JAN'},
        2:{'month': 'February','days': 28,'code': 'FEB'},
        3:{'month': 'March','days': 31, 'code': 'MAR'},
        4:{'month': 'April','days': 30, 'code': 'APR'},
        5:{'month': 'May','days': 31, 'code': 'MAY'},
        6:{'month': 'June','days': 30, 'code': 'JUN'},
        7:{'month': 'July','days': 31, 'code': 'JUL'},
        8:{'month': 'August','days': 31, 'code': 'AUG'},
        9:{'month': 'September','days': 30, 'code': 'SEP'},
        10:{'month': 'October','days': 31,'code': 'OCT'},
        11:{'month': 'November','days': 30, 'code': 'NOV'},
        12:{'month': 'December','days': 31, 'code': 'DEC'}
        }

def clean(cal: list):
    cleaned_cal = []
    for i in cal:
        cleaned_entry = i
        for j in ['year','month','day','start','end','priority','difficulty','rating']:
            cleaned_entry[j] = int(i[j]) if i[j] else None
        cleaned_cal.append(cleaned_entry)
    return cleaned_cal

def create_empty_calendar(month_number: int)->list:
    """
    creates the template for the month corresponding to month_number, 
    puts it in a list of dicts. Each row is half an hour, each column 
    is a day of the month.
    """
    
    CALENDAR = []
    for i in range(48):
        row = {}
        if i%2 == 0:
            hour = str(i//2)+':00'
        else:
            hour = str(i//2)+':30'
        row['hour'] = hour
        for j in range(1,DICT_MONTHS[month_number]['days']+1,1):
             row[DICT_MONTHS[month_number]['code']+ ' ' + str(j)] = ''  #will eventually hold event name for that day 
        CALENDAR.append(row)
    return(CALENDAR)

def hourToPosition(hour):
    """
    convert a given hour to the position of that hour in a day, divided in 30-minute periods
    """
    HourMin = 0
    HourMax = 2330
    PosMin = 0
    PosMax = 47
    return round((((hour - HourMin) * (PosMax - PosMin)) / (HourMax - HourMin)) + PosMin)

def dayFormat(day_number,month_number):
    return f"{DICT_MONTHS[month_number]['code']} {day_number}"

def write(file_name: str, final_calendar: list)->None:
    """
    writes the final calendar (list of dicts) to a csv table named file_name 
    which will be located in the folder containing the code
    """
    with open(file_name,'w',encoding="utf-8") as fp: #force the encoding to be utf-8 to avoid display bugs
        writer = csv.DictWriter(fp, fieldnames = list(final_calendar[0].keys()))
        writer.writeheader()
        writer.writerows(final_calendar)