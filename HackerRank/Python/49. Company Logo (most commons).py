#!/bin/python3
import operator
import math
import os
import random
import re
import sys
def CompanyLogo(s):
    dict={}
    for j in li:
        dict[j]=li.count(j)
    cd = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    for j,k in cd[:3]:
        print(j,end=" ")
        print(k)
if __name__ == '__main__':
    s =str(input())
    li=[]
    for i in s:
        li.append(i)
        li.sort()
    CompanyLogo(s)