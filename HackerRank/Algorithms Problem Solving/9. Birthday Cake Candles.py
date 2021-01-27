#!/bin/python3
import math
import os
import random
import re
import sys
import time
# Complete the birthdayCakeCandles function below.

def birthdayCakeCandles(ar):
    start = time.time()
    count=0
    for i in range(len(ar)):
        m=max(ar)
        if ((ar[i])==m):
            count=count+1
    print(count)
    end = time.time()
    print("elapse time:",(end-start))
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    #fptr.write(str(result) + '\n')
    #fptr.close()
