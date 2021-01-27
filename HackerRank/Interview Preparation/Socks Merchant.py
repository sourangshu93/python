#!/bin/python3
import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\newfile.txt"
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d={}
    for i in ar:
        d[i]=ar.count(i)
    count=0
    for k in d.values():
        j=k//2
        count=count+j
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()