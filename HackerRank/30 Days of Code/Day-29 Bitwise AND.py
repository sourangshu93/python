#!/bin/python3
import math
import os
import random
import re
import sys
import itertools
def BitwiseAnd(n,k):
    print (max([a&b for a,b in itertools.combinations(range(1,n+1), 2) if a&b < k]))
    AB=list(itertools.combinations(range(1,n+1),2))
    S=[]
    for ab in AB:
        if ab[0]<ab[-1] and (ab[0]&ab[-1])<k:
            S.append((ab[0]&ab[-1]))
    print(max(S))
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        BitwiseAnd(n,k)