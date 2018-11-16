# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:31:54 2018

@author: Kevin
"""

class Event:
    """ 
    A class for creating events
    
    """
    
#    def __init__(self, title: str, year: int, month: int, day: int, start: int, end: int, pref: int, desc: str = ''):
#        self._title = title
#        self._year = year
#        self._month = month
#        self._day = day
#        self._start = start
#        self._end = end
#        self._desc = desc
#        self._pref = pref
    
    def __init__(self, title: str, day: int, start: int, end: int, pref: int, desc: str = ''):
        """
        Create an event with the date, the hours, the priority rating and an optional description
        """
        self.title = title
        self.day = day
        self.start = start
        self.end = end
        self.desc = desc
        self.pref = pref
    
    def __str__(self):
        return f'{self.title} - Start time: {self.start}, End time: {self.end}, Pref: {self.pref}, Desc: {self.desc}'
#    @property
#    def title(self):
#        return self._title
#    @title.setter
#    def title(self,val):
#        self._title = str(val)  
    
#    @property
#    def year(self):
#        return self._year
#    @year.setter
#    def year(self,val):
#        if type(val) == int and val > -1: 
#            self._year = val
#        else:
#            raise ValueError('Please enter a valid year, i.e integral and positive')
#    
#    @property
#    def month(self):
#        return self._month
#    @month.setter
#    def month(self,val):
#        if type(val) == int and val < 13 and val > 0: 
#            self._month = val
#        else:
#            raise ValueError('Please enter a valid month, i.e between 1 and 12')
     
#    @property
#    def day(self):
#        return self._day
#    @day.setter
#    def day(self,val):
#        #TODO: check if year is bissextile, the number of days in a month
#        if type(val) == int and val < 32:
#            self._day = val
#        else:
#            raise ValueError('Please enter a valid day, i.e between 1 and 31')
#        
#    @property
#    def start(self):
#        return self._start
#    @start.setter
#    def start(self,val):
#        if type(val) == int:
#            self._start = val
#        else:
#            raise ValueError('Please enter an hour in the correct format.')        
#    
#    @property
#    def end(self):
#        return self._end
#    @end.setter
#    def end(self,val):
#        if val < self._start:
#            raise ValueError('Please enter an hour after the start of the event.')  
#        if type(val) == int:
#            self._end = val
#        else:
#            raise ValueError('Please enter an hour in the correct format.')
#    
#    @property
#    def desc(self):
#        return self._desc
#    @desc.setter
#    def desc(self,text):
#        self._desc = str(text)
#        
#    @property
#    def pref(self):
#        return self.pref
#    @pref.setter
#    def pref(self,val):
#        self.pref = val
    
    
class Academic(Event):
    pass

class Professional(Event):
    pass

class Cultural(Event):
    pass