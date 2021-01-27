import itertools
import numpy
from itertools import combinations
def triangles(N,B1,B2):
    n1=(int(N)+1)
    l=list(map(int,numpy.arange(1,n1)))
    l.remove(int(B1))
    l.remove(int(B2))
    print(len(list(combinations(l,3))))

if __name__=="__main__":
    t=int(input())
    for T in range(t):
        N,B1,B2=input().split()
        triangles(N,B1,B2)