#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    noa=0
    noo=0
    lia=[]
    lio=[]
    for i in apples:
        dist=(i+(a))
        lia.append(dist)
    for j in lia:
        if (t>=j>=s):
            noa+=1
    for k in oranges:
        dist1=(k+(b))
        lio.append(dist1)
    for l in lio:
        if (t>=l>=s):
            noo+=1
    print(noa)
    print(noo)
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
