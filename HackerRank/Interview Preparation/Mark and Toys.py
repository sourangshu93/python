#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\new.txt"
# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    price=0
    count=0
    for p in prices:
        price=price+p
        if price <=k:
            count+=1
    print(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()