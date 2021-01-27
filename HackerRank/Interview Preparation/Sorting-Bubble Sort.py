#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps=0
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                swaps+=1
    print("Array is sorted in",swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
