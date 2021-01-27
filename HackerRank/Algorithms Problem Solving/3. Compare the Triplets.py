#!/bin/python3

import math
import os
import random
import re
import sys
os.environ["OUTPUT_PATH"]="C:\\Users\\kundus6\\Desktop\\newfile.txt"
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice=0
    bob=0
    for (i,j) in zip(a,b):
        if i<j:
            bob=bob+1
        if i>j:
            alice=alice+1
        if i==j:
            alice=alice+0
            bob=bob+0
    print(alice,bob)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()