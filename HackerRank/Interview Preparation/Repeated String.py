#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\Newfile.txt"
# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s)==1 and "a"in s:
        print(n)
    if 'a' in s and len(s)>1:
        p=n//len(s)
        q=s.count('a')
        r=n%len(s)
        t=s[0:r]
        u=t.count('a')
        print(q*p+u)
    if 'a' not in s:
        print(0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()