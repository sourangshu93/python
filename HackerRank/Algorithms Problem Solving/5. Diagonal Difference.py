#!/bin/python3
import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    # Write your code here
    na1=[]
    na2=[]
    sum1=0
    sum2=0
    #From left to right diagonal w and right to left diagonal x
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            w=((arr[j])[j])
            x=((arr[j])[-(j+1)])
            na1.append(w)
            na2.append(x)
    d1=na1[0:len(arr)]
    d2=na2[0:len(arr)]
    for k in range(len(d1)):
        sum1=sum1+d1[k]
    for l in range(len(d2)):
        sum2=sum2+d2[l]
    print(abs(sum1-sum2))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    #fptr.write(str(result) + '\n')
    #fptr.close()