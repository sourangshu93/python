# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
from collections import defaultdict
def DefaultDict(s,d,l1):
    for l in l1:
        if len(d[l])>0:
            print(' '.join(d[l]))
        else:
            print("-1")
        
if __name__ == '__main__':
    s=list(map(int,input().split()))
    d = defaultdict(list)
    l1=[]
    for n in range(s[0]):
        d[(input())].append(str(n+1))
    for m in range(s[1]):
        l1.append(input())
    DefaultDict(s,d,l1)