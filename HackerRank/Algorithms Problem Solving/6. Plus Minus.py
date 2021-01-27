#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the plusMinus function below.
def plusMinus(arr):
    plus=0
    minus=0
    zero=0
    for i in range (0,n):
        if arr[i]>0:
            plus=plus+1
    for j in range(0,n):
        if arr[j]<0:
            minus=minus+1
    for k in range(0,n):
        if arr[k]==0:
            zero=zero+1
    print("{:.6f}".format(plus/n))
    print("{:.6f}".format(minus/n))
    print("{:.6f}".format(zero/n))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
