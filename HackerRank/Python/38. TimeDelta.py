#!/bin/python3
import math
import os
import random
import re
import sys
import time
import calendar
import datetime
from datetime import timedelta
def time_delta(t1, t2):
    l=list(calendar.month_name)
    l1=(t1.split())
    l11=l1[1:-1]
    nt1=" ".join(l11)
    l2=(t2.split())
    l12=l2[1:-1]
    nt2=" ".join(l12)
    obj1 = time.strptime(nt1, "%d %b %Y %H:%M:%S")
    obj2 = time.strptime(nt2, "%d %b %Y %H:%M:%S")
    tsec1=(time.mktime(obj1))
    tsec2=(time.mktime(obj2))
    timezone1=l1[-1]
    timezone2=l2[-1]
    timezone11=timezone1[1:]
    timezone12=timezone2[1:]
    timez1=("{:.2f}".format(float(abs(int(timezone11)/100))))
    timez2=("{:.2f}".format(float(abs(int(timezone12)/100))))
    q1=timez1.split(".")
    q2=timez2.split(".")
    q1.append("00")
    q2.append("00")
    q11=":".join(q1)
    q12=":".join(q2)
    obj13=datetime.datetime.strptime(q11, "%H:%M:%S")
    obj14=datetime.datetime.strptime(q12, "%H:%M:%S")
    print(obj13)
    print(obj14)
    print(datetime.datetime.time(obj13))
    obj3=(datetime.datetime.time(obj13))
    obj4=(datetime.datetime.time(obj14))
    time_zero=datetime.datetime.strptime('00:00:00', '%H:%M:%S')
    timeinsec=(tsec1-tsec2)
    if (timezone1[0]=="+" and timezone2[0]=="+"):
        print((str(obj3)).split(" "))
        m=(obj3-obj4)
        p1=(str(m)).split(":")
        print(p1)
        timezinsec=((abs(int(p1[0])))*3600+(int(p1[1])*60))
        print(abs(int(timeinsec-timezinsec)))
    if (timezone1[0]=="-" and timezone2[0]=="+"):
        m1=((obj3 - time_zero + obj4).time())
        p2=(str(m1)).split(":")
        timezinsec=((int(p2[0]))*3600+(int(p2[1])*60))
        print(abs(int(abs(timeinsec))-int(timezinsec)))
    if timezone1[0]=="-" and timezone2[0]=="-":
        p3=(str(obj3-obj4)).split(":")
        timezinsec=((int(p3[0]))*3600+(int(p3[1])*60))
        print(abs(int(timeinsec-timezinsec)))
    if (timezone1[0]=="+" and timezone2[0]=="-"):
        m2=((obj3 - time_zero + obj4).time())
        p4=(str(m2)).split(":")
        timezinsec=((int(p4[0]))*3600+(int(p4[1])*60))
        print(abs(int(abs(timeinsec)-timezinsec)))
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        #Sat 02 May 2015 19:54:36 +0530
        #Fri 01 May 2015 13:54:36 -0000
        
