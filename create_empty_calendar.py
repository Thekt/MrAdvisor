def create_empty_calendar(month_number: int)->list:
"""creates the template for the month corresponding to month_number, puts it in a list of dicts. Each row is half an hour, each column is a day of the month."""
    dict_months = {
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
    CALENDAR = []
    for i in range(48):
        row = {}
        #if i%2 == 0:
        #    hour = str(i//2)+':00'
        #else:
        #    hour = str(i//2)+':30'
        if i%2 == 0:
            if i == 0:
                hour = '12:00 AM'
            elif 0 < i <= 22:
                hour = str(i//2)+':00 AM'
            elif i == 24:
                hour = '12:00 PM'
            else:
                hour = str(i//2 - 12)+':00 PM'
        else:
            if i == 1:
                hour = '12:30 AM'
            elif 1 < i <= 23:
                hour = str(i//2)+':30 AM'
            elif i == 25:
                hour = '12:30 PM'
            else:
                hour = str(i//2 - 12)+':30 PM'
        row['hour'] = hour
        for j in range(1,dict_months[month_number]['days']+1,1):
             row[dict_months[month_number]['code']+ ' ' + str(j)] = '-'  #will eventually hold event name for that day 
        CALENDAR.append(row)
    return(CALENDAR)
    #filename = dict_months[month_number]['month']+'_Calendar.csv'
    #calendar_writer(filename, CALENDAR)
