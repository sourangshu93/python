#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    arr2=[]
    for i in range(len(arr)-2):
        for j in range (len(arr)-2):
            a1=(arr[i][j:j+3])
            a1.append(arr[i+1][j+1])
            a2=(arr[i+2][j:j+3])
            a=a1+a2
            arr2.append(a)
    s=[]
    for k in arr2:
        s.append(sum(k))
    print(max(s))
