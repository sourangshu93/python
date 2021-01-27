#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import time
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\Newfile.txt"
# Complete the rotLeft function below.
def rotLeft(a, d):
    l=[]
    if d==0:
        return(a)
    if d==1:
        for i in range(len(a)-1):
            l.append(a[i+1])
        l.append(a[0])
        return(l)
    else:
        return(rotLeft(rotLeft(a,1),d-1))
# Complete the rotRight function below.
def rotRight(a, d):
    l1=[]
    if d==0:
        return a
    if d==1:
        l1.append(a[-1])
        for i in range(len(a)-1):
            l1.append(a[i])
        return(l1)
    else:
        return(rotRight(rotRight(a,1),d-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    if d>997:
        result=rotRight(a,abs(n-d))
    else:
        result=rotLeft(a,d)
    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()