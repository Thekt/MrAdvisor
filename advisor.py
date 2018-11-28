# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:56:29 2018

@author: Kevin
"""

def restructure(month_cal: list, month_number: int) -> list:
    """
    turn a month(list) consistend in events(dict) into a month(list) 
    consisted in days(list), each days consisted in events(list)
    """
    new_month_cal = [[] for i in range(month_number)]
    for i in month_cal:
        new_month_cal[i['day']].append(i)
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
#    event1['attend'] = 1
#    event2['attend'] = 0
    pass
    
def advisor(month_cal: list, month_number: int) -> list:
    """
    choose the events to attend in case of conflicting schedules for a particular month
    """
    month_cal = restructure(month_cal, month_number)
    ml = len(month_cal)
    
    #Detecting clashes
    for d in month_cal: #checking each day
        if d:
            dl = len(d)
            for e1 in range(dl): #checking each event in a day
                for e2 in range(e1+1, dl):
                    if hasClash(d[e1],d[e2]):
                        flag(d[e1],d[e2])
                        solve(d[e1],d[e2])

#Competing events that clash for the same slot with each other
if ca_len > 1:
    for i in range(ca_len-1):
        if calendar[i]['clash'] != 0 and calendar[i]['result'] == 1:
            for j in range(i+1, ca_len):
                if calendar[i]['result'] == 1 and calendar[j]['clash'] == calendar[i]['clash']:
                    if calendar[i]['category'] == 'acad' and calendar[j]['category'] == 'acad':
                        if acad_fin_score(i) > acad_fin_score(j):
                            calendar[j]['result'] = 0
                        elif acad_fin_score(i) == acad_fin_score(j):
                            calendar[i]['result'] = 0
                            calendar[j]['result'] = 0
                            calendar[i]['tie'] = 1
                            calendar[j]['tie'] = 1
                        else:
                            calendar[i]['result'] = 0
                    elif calendar[i]['category'] == 'acad' and calendar[j]['category'] != 'acad':
                        if acad_fin_score(i) > calendar[j]['priority']:
                            calendar[j]['result'] = 0
                        elif acad_fin_score(i) == calendar[j]['priority']:
                            calendar[i]['result'] = 0
                            calendar[j]['result'] = 0
                            calendar[i]['tie'] = 1
                            calendar[j]['tie'] = 1
                        else:
                            calendar[i]['result'] = 0
                    elif calendar[i]['category'] != 'acad' and calendar[j]['category'] == 'acad':
                        if calendar[i]['priority'] > acad_fin_score(j):
                            calendar[j]['result'] = 0
                        elif calendar[i]['priority'] == acad_fin_score(j):
                            calendar[i]['result'] = 0
                            calendar[j]['result'] = 0
                            calendar[i]['tie'] = 1
                            calendar[j]['tie'] = 1
                        else:
                            calendar[i]['result'] = 0
