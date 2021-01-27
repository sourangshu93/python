# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
import calendar

def DayOnThatDate(date):
    year=int(date[2])
    month=int(date[0])
    day=int(date[1])
    d=(calendar.weekday(year,month,day))
    weekdays=(list(calendar.day_name))
    for i,e in enumerate(weekdays):
        if i==d:
            print(e.upper())
if __name__ == '__main__':
    date=list(map(str,input().split()))
    DayOnThatDate(date)
