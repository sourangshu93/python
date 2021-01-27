#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrangeStudents' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#os.environ['OUTPUT_PATH']="C:\\Users\\kundus6\\Desktop\\new.txt"
def arrangeStudents(a, b):
    # Write your code here
    st=[]
    if a[0]<b[0]:
        for i in range(n):
            st.append(a[i])
            st.append(b[i])
    if a[0]>b[0]:
        for i in range(n):
            st.append(b[i])
            st.append(a[i])
    st1=sorted(st)
    if st1==st:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        arrangeStudents(a, b)
        #fptr.write(result + '\n')
    #fptr.close()