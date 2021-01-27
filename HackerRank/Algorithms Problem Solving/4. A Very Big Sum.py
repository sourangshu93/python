#!/bin/python3

import math
import os
import random
import re
import sys
os.environ["OUTPUT_PATH"]="C:\\Users\\kundus6\\Desktop\\sum.txt"
# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum=0
    for i in range (ar_count):
        sum=sum+ar[i]
    print(sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
