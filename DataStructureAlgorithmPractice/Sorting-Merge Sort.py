#!/bin/python3
import sys

def MergeSort(a):
    # Write Your Code Here
    if len(a)>1:
        mid=len(a)//2
        leftarray=a[:mid]
        rightarray=a[mid:]
    # Using reccursion to break the dataset further.
        MergeSort(leftarray)
        MergeSort(rightarray)
    # Perform the merging of the broken datasets
        i=0 # Leftarray index
        j=0 # Rightarray index
        k=0 # Merging index
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                a[k]=leftarray[i]
                i=i+1
            else:
                a[k]=rightarray[j]
                j=j+1
            k=k+1
    # If the left array still has value
        while i <len(leftarray):
            a[k]=leftarray[i]
            i=i+1
            k=k+1
    # If the right array still has value
        while j <len(rightarray):
            a[k]=rightarray[j]
            j=j+1
            k=k+1
if __name__ == '__main__':
    a = list(map(int, input().strip().split(' ')))
    MergeSort(a)
    print(a)