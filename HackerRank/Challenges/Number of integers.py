#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getNumberOfIntegers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING L
#  2. STRING R
#  3. INTEGER K
#
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\new.txt"
def getNumberOfIntegers(L, R, K):
    l=[]
    s1="[1-9]"*K+"$"
    s2="[1-9]"*K+"[0]{1,}"
    pattern1=re.compile(s1)
    pattern2=re.compile(s2)
    for i in range(int(L)+1,int(R)+1):
        if re.match(pattern1,str(i)) or re.match(pattern2,str(i)):
            l.append(i)
    print(l)
    print(len(l))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    L = input()
    R = input()
    K = int(input().strip())
    ans = getNumberOfIntegers(L, R, K)
    fptr.write(str(ans) + '\n')
    fptr.close()
