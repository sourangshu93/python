#!/bin/python3
import os
import sys
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour=(s[0:2])
    min=(s[3:5])
    sec=(s[6:8])
    last=s[-2:]
    if (last=="PM") and (int(hour)!=12):
        newhour=int(hour)+12
        print("{}:{}:{}".format(newhour,min,sec))
    if (last=="PM") and (int(hour)==12):
        print("{}:{}:{}".format(hour,min,sec))
    if last=='AM'and ((int(hour)+12)!=24):
        print("{}:{}:{}".format(hour,min,sec))
    if (last=="AM") and ((int(hour)+12)==24):
        hr="00"
        print("{}:{}:{}".format(hr,min,sec))
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)