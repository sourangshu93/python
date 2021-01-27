# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
from collections import Counter
def CollectionsCounter(X,s,N,x):
    sell=0
    for i in l:
        if int(i[0]) in s:
            sell=sell+i[1]
            s.remove(i[0])
    print("Total Sell of the Day:",sell)
if __name__ == '__main__':
    X=int(input("No of Shoes:"))
    s=list(map(int,input("Size List:").split()))
    N=int(input("No Of customers:"))
    l=[]
    for n in range (N):
        x=list(map(int,input("Customer and Desired Size/Price:").split()))
        l.append(x)
    q=CollectionsCounter(X,s,N,x)
        
        