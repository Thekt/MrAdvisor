# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:27:10 2018

@author: Kevin
"""
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 1000)
class Calendar:
    """
    Create a calendar which contains the events
    """
    def __init__(self):
        self.cal =  [[0]*48]*31
    
    def add(self,event):
        if not self.cal[event.day][event.start] or self.cal[event.day][event.start][1] < event.pref:
            self.cal[event.day][event.start] = [event.title,event.pref,event.desc]
                
    def delete(self,event):
        """
        Delete an event in the calendar
        """
        #TODO: check for event.title() in the current calendat
        #TODO: check also regex to search for title: 'Did you mean...?'
        del self.cal[event.day][event.start]
    
    def display(self,day):
        """
        Search for a date and return the events scheduled that day
        """
        hours = pd.Series([float(i/2) for i in range(48)])
        return pd.DataFrame(self.cal[day], index=hours, columns=[day])
        
    def advisor(event):
        pass
    
          