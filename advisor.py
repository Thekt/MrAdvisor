# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:56:29 2018

@author: Kevin
"""
from random import randint

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

def restructure(month_cal: list, month_number: int) -> list:
    """
    turn a month(list) consistend in events(dict) into a month(list) 
    consisted in days(list), each days consisted in events(list)
    """
    new_month_cal = [[] for i in range(DICT_MONTHS[month_number]['days'])]
    for i in month_cal:
        new_month_cal[i['day']-1].append(i)
    return new_month_cal

def hasClash(event1: dict, event2: dict) -> bool:
    start1,end1 = event1['start'],event1['end']
    start2,end2 = event2['start'],event2['end']
    x = range(start1, end1+30,30)
    y = range(start2, end2+30,30)
    xs = set(x)
    return len(xs.intersection(y)) != 0
            
def flag(event1: dict, event2: dict):
    event1['clash'].append(event2['id'])
    event2['clash'].append(event1['id'])

def acad_score(e):
    """
    Determine the score of academic ('A') events
    """
    return e['priority'] + e['priority'] * e['difficulty'] * (e['rating'] ** 2) / 10000

def solve(event1: dict, event2: dict):
    b1 = (event1['category'] == 'A')
    b2 = (event2['category'] == 'A')
    if b1 and b2: #two courses overlap
        s1 = acad_score(event1)
        s2 = acad_score(event2)
        if s1 == s2: #if tie, we go to the most challenging course 
            event1['attend'] = (event1['difficulty'] > event2['difficulty'])
            event2['attend'] = 1 - event1['attend'] 
        else:
            event1['attend'] = (s1 > s2)
            event2['attend'] = 1 - event1['attend']
    elif (b1 and not b2) or (not b1 and b2): #one course and one event overlap
        f1,f2 = event1,event2
        #switch event number ta always have e1 as academic
        if not b1:
            f1,f2 = f2,f1
        s1 = acad_score(f1)
        s2 = f2['priority']
        if s1 == s2: #if tie, we go to the course 
            f1['attend'],f2['attend'] = 1,0
        else:
            f1['attend'] = (s1 > s2)
            f2['attend'] = 1 - event1['attend']
        
    else: #two events (others than courses) overlap
        s1,s2 = event1['priority'],event2['priority']
        c1,c2 = event1['category'],event2['category']
        
        if s1 == s2:
            if c1 == c2: #pick a random one
                event1['attend'] = randint(0,2) 
                event2['attend'] = 1 - event1['attend']
            else: #preference to professional events
                event1['attend'] = (c1 == 'P')
                event2['attend'] = (c2 == 'P')
        else: 
            event1['attend'] = (s1 > s2)
            event2['attend'] = 1 - event1['attend']
                
    
    
def advisor(month_cal: list, month_number: int) -> list:
    """
    choose the events to attend in case of conflicting schedules for a particular month
    """
    month_cal = restructure(month_cal, month_number)
    
    #Detecting clashes
    for d in month_cal: #checking each day
        if d: #list not empty
            dl = len(d)
            for e1 in range(dl): #checking each event in a day
                for e2 in range(e1+1, dl):
                    if hasClash(d[e1],d[e2]):
                        flag(d[e1],d[e2])
                        solve(d[e1],d[e2])