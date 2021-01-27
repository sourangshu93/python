# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import os
if __name__=="__main__":
    N=int(input())
    d={}
    for n in range(N):
        s=input().split()
        d[s[0]]=s[-1]
    inputs=sys.stdin
    for i in inputs:
        try:
            q=i.replace("\n","")
            m=d[q]
            print("{}={}".format(q,m))
        except KeyError:
            print("Not found")
    