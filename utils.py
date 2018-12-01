import calendar_tools
import random
import csv
from datetime import timedelta, datetime

#create empty timeslots
start_date = datetime(2018, 1, 1, 0, 0, 0)
list_time_slot = []
for td in (start_date + timedelta(minutes=30*it) for it in range(49)):
    list_time_slot.append(td.strftime("%H%M"))
     
def create_clash(filename: str): 
    """
    Create random clash events and write the events in a file  
    """
    category = ['A', 'P', 'C']
    year = 2018
    month = random.randint(1,12)
    day = random.randint(1,calendar_tools.dayInMonth(month))
    
    time_1_slot = random.randint(0,46)
    time_1 = list_time_slot[time_1_slot]
    time_1_end_slot = random.randint(time_1_slot+1, 48)
    time_1_end = list_time_slot[time_1_end_slot]
    
    time_2_slot = random.randint(time_1_slot, time_1_end_slot-1)
    time_2 = list_time_slot[time_2_slot]
    time_2_end_slot = random.randint(time_2_slot+1, 48)
    time_2_end = list_time_slot[time_2_end_slot]
    
    event_name_1 = f'Event Number {random.randint(0,6000)}'
    cat_no_1 = random.randint(0,2)
    category_name_1 = category[cat_no_1]
    priority_1 = random.randint(0,10)
    difficulty_1 = random.randint(0,10)
    rating_1 = random.randint(0,10)
    
    event_name_2 = f'Event Number {random.randint(0,6000)}'
    cat_no_2 = random.randint(0,2)
    category_name_2 = category[cat_no_2]
    priority_2 = random.randint(0,10)
    difficulty_2 = random.randint(0,10)
    rating_2 = random.randint(0,10)
    
    with open(filename, 'a', newline='') as cal:
        cal_writer = csv.writer(cal, delimiter=',')
        cal_writer.writerow([event_name_1, category_name_1, year, month, day, time_1, time_1_end, priority_1, difficulty_1, rating_1])
        cal_writer.writerow([event_name_2, category_name_2, year, month, day, time_2, time_2_end, priority_2, difficulty_2, rating_2])

          
#pass number of clash events needed        
def create_clashes(n: int, filename: str = 'sample_calendar.csv'):
    with open(filename, 'w', newline='') as cal:
        cal_writer = csv.writer(cal, delimiter=',')
        cal_writer.writerow(['title', 'category', 'year', 'month', 'day', 'start', 'end', 'priority', 'difficulty', 'rating'])
    for i in range(n):
        create_clash(filename)
    print(filename)
    
create_clashes(100)
       
        
   
        