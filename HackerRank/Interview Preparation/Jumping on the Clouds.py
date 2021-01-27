#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\newfile.txt"
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    s=("".join(c))
    m=re.findall(r"([0]{1,})",s)
    count=0
    for i in m:
        if len(i)>=2:
            j=len(i)//2
            count=count+j
    print(count)
    print(len(m)+count-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(str, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()