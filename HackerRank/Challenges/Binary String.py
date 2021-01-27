#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER d
#
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\new.txt"
def minimumMoves(s, d):
    # Write your code here
    li=[]
    for i in range(len(s)):
        if len(s[i:i+d])==d:
            li.append(s[i:i+d]) 
    m="0"
    print(li.count(m*d))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    d = int(input().strip())
    result = minimumMoves(s, d)
    fptr.write(str(result) + '\n')
    fptr.close()