#!/bin/python3
# Bubble sort
import sys
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count=0
for i in range(n-1,0,-1):
    for j in range (i):
        if a[j]>a[j+1]:
            tmp=a[j]
            a[j]=a[j+1]
            a[j+1]=tmp
            count=count+1
print ("Sorted Array:",a)
print("The array has been sorted in",count,"swaps.")