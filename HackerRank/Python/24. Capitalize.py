#!/bin/python3
import math
import os
import random
import re
import sys
os.environ["OUTPUT_PATH"]="C:\\Users\\kundus6\\Desktop\\newfile.txt"
# Complete the solve function below.
def solve(s):
    w=s.split(" ")
    li=[]
    for i in range (0,(len(w))):
        c=w[i].capitalize()
        li.insert(i,c)
        q=" ".join(li)
    print(q)
    return q
if __name__ == '__main__':
    fptr=open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result+"\n")
    fptr.close()