#!/bin/python3
import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\newfile.txt"
# Complete the countingValleys function below.
def countingValleys(n, s):
    sealevel=0
    valey=0
    for i in s:
        if i=="U":
           print("/")
        if i=="D":
            print("\ ",end="")
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    countingValleys(n, s)
    #fptr.write(str(result) + '\n')
    #fptr.close()