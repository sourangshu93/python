#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q1=q.copy()
    swaps=0
    l1=[]
    for i in range (n-1,0,-1):
        for j in range (i):
            if q[j]>q[j+1]:
                tmp=q[j]
                q[j]=q[j+1]
                q[j+1]=tmp
                swaps=swaps+1
print(swaps)
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)