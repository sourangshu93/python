#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    kang1=[]
    kang2=[]
    for i in range(x1,100000000000,v1):
        kang1.append(i)
    for j in range(x2,100000000000,v2):
        kang2.append(j)
    li1=[]
    for (k,l) in zip(kang1,kang2):
        if k==l:
            li1.append("True")
        else:
            li1.append("False")
    if "True" in li1:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    #fptr.write(result + '\n')
    #fptr.close()
