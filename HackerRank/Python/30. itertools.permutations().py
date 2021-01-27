# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import os
from itertools import permutations
def Permutation(s):
    a=int(s[1])
    b=s[0]
    q=list(permutations(b,a))
    q.sort()
    for i in q:
        j=list(i)
        k="".join(j)
        print(k)
if __name__ == '__main__':
    s=list(map(str,input().split()))
    Permutation(s)