#!/bin/python3

import math
import os
import random
import re
import sys
#os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\new.txt"
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    for i in range(len(arr)):
        m=min(arr[i:])
        ind=arr.index(m)
        if m!=arr[i]:
            t=arr[i]
            arr[i]=m
            arr[ind]=t
            count=count+1
        else:
            pass
    print(count)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    minimumSwaps(arr)