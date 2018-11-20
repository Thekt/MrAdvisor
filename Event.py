# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:31:54 2018

@author: Kevin
"""


class Event:
    
    #classification of the months of the year accordig to the number of days, Feb is a special case
    MORE_DAYS = [1,3,5,7,8,10,12]
    LESS_DAYS = [4,6,9,11]
    
    """ 
    A class for creating events
    
    """   
    def __init__(self, title: str, year: int, month: int, day: int, start: int, end: int, pref: int, desc: str = ''):
        """
        Create an event with the date, the hours, the priority rating and an optional description
        """
        self.title = title
        self.year = year
        self.month = month
        self.day = day
        self.start = start
        self.end = end
        self.desc = desc
        self.pref = pref
        self.decision = 1
    
    def __str__(self):
        return f'{self.title} - Start time: {self.start}, End time: {self.end}, Pref: {self.pref}, Desc: {self.desc}'

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,val):
        self._title = str(val)  
    
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,val):
        if type(val) == int and val > -1: 
            self._year = val
        else:
            raise ValueError('Please enter a valid year, i.e integral and positive')
    def isleap(self):
        y = self.year
        return y%4==0 and y%100==0 and y%400==0
    
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self,val):
        if type(val) == int and val < 13 and val > 0: 
            self._month = val
        else:
            raise ValueError('Please enter a valid month, i.e between 1 and 12')
     
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self,val):
        if type(val) != int and val < 1:
            raise ValueError('Please enter an integer day')
        elif self.month in self.MORE_DAYS and val > 31: #Months with 31 days
            raise ValueError('Please enter a valid day, i.e. beween 1 and 31')
        elif self.month in self.LESS_DAYS and val > 30: #Months with 30 days
            raise ValueError('Please enter a valid day, i.e. beween 1 and 30')
        #February case
        elif self.isleap():
            if val > 29:
                raise ValueError('Please enter a valid day, i.e. beween 1 and 29')
        elif val > 28:
            raise ValueError('Please enter a valid day, i.e. beween 1 and 28')
        else:
            self._day = val
      
    
        
    @property
    def start(self):
        return self._start
    @start.setter
    #hour format : 9am = 0900, 9:54am = 0954
    def start(self,val):
        if type(val) == int and len(str(val))==4:
            self._start = val
        else:
            raise ValueError('Please enter an hour in the correct format, i.e. 9:54am -> 0954')        
    
    @property
    def end(self):
        return self._end
    @end.setter
    def end(self,val):
        if val < self._start:
            raise ValueError('Please enter an hour after the start of the event.')  
        elif type(val) == int and len(str(val))==4:
            self._end = val
        else:
            raise ValueError('Please enter an hour in the correct format.')
    
    @property
    def desc(self):
        return self._desc
    @desc.setter
    def desc(self,text):
        self._desc = str(text)
        
    @property
    def pref(self):
        return self.pref
    @pref.setter
    def pref(self,val):
        #scale of preference between 0 and 10
        if type(val) == int and val > -1 and val < 10:
            self.pref = val
        else:
            raise ValueError('Please enter a preference score between 0 and 10, both included.')
    
    
class Academic(Event):
    pass

class Professional(Event):
    pass

class Cultural(Event):
    pass