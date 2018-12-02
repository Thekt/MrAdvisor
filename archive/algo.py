#INITIALIZATION
#dic_i
#dic_i['clash'] = 0
#dic_i['result'] = 1
#dic_i['tie'] = 0
#calendar = [dic_1, dic_2, ... dic_n]


dic_1 = {
    'id':1,
    'title': 'Hilarious Python',
    'category':'acad',
    'date':2018-11-26,
    'start':1930,
    'end':2200,
    'venue':'IABXXX',
    'priority':10,
    'course_diff':10,
    'prof_rating':10,
    'clash':0,
    'result':1,
    'tie':0
}

dic_2 = {
    'id':2,
    'title': 'McKinsey par interview',
    'category':'career',
    'date':2018-11-27,
    'start':1830,
    'end':2000,
    'venue':'Bar of darkness',
    'priority':9,
    'course_diff':'whatever',
    'prof_rating':'does not even matter',
    'clash':0,
    'result':1,
    'tie':0
}

calendar = [dic_1, dic_2]
ca_len = len(calendar)


#Detecting clashes
if ca_len > 1:
    for i in range(ca_len-1):
        if calendar[i]['clash'] == 0:
            for j in range(i+1, ca_len):
                if calendar[i]['start'] < calendar[j]['end'] < calendar[i]['end'] or calendar[j]['start'] < calendar[i]['end'] < calendar[j]['end'] or calendar[j]['start'] <= calendar[i]['start'] < calendar[i]['end'] <= calendar[j]['end'] or calendar[i]['start'] <= calendar[j]['start'] < calendar[j]['end'] <= calendar[i]['end']:
                    clash_id = min(calendar[i]['id'], (calendar[j]['id']))
                    calendar[i]['clash'] = clash_id
                    calendar[j]['clash'] = clash_id

#Printing clash results
print("clash results:")
for item in calendar:
    print(f"item {item['id']}: {item['clash']}")


#Determining the final score of 'acad' events
def acad_fin_score(i):
    return calendar[i]['priority'] + calendar[i]['priority'] * calendar[i]['course_diff'] * (calendar[i]['prof_rating'] ** 2) / 10000


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
                            
