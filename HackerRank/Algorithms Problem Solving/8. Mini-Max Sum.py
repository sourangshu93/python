#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the miniMaxSum function below.

def miniMaxSum(arr):
    arr1=arr.copy()
    arr2=arr.copy()
    na1=[]
    na2=[]
    maxsum=0
    minsum=0
    for i in range (len(arr1)-1):
        q=max(arr1)
        arr1.remove(q)
        na1.insert(i,q)
    for j in range (len(na1)):
        maxsum=maxsum+na1[j]
    for k in range (len(arr2)-1):
        r=min(arr2)
        arr2.remove(r)
        na2.insert(k,r)
    for l in range (len(na2)):
        minsum=minsum+na2[l]
    print(minsum,maxsum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
