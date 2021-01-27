#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\new.txt"
# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr2=[]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            a1=(arr[i][j:j+3])
            a1.append(arr[i+1][j+1])
            a2=(arr[i+2][j:j+3])
            a=a1+a2
            arr2.append(a)
    s=[]
    for k in arr2:
        s.append(sum(k))
    print(max(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()