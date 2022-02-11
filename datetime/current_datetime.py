#Python Program to print the current Date and Time.

from datetime import datetime
current_dt = datetime.now()
print(current_dt)    #Complete Date and Time
print(current_dt.day)   #Only Date
print(current_dt.month)     #Only Month
print(current_dt.year)          #Only Year
print(current_dt.hour)              #Only Hour
print(current_dt.minute)                #Only minutes
print(current_dt.second)                    #Only Seconds



