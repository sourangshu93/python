#!/bin/python3

import math
import os
import random
import re
import sys

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
    print(("The list is sorted in {} swaps").format(count))
    return arr
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(minimumSwaps(arr))