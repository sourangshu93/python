from functools import reduce
import numpy
from math import gcd
def lcm(l):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, l, 1)
if __name__=="__main__":
    T=int(input())
    n=list(map(int,input().strip().split()))
    l=list(map(int,input().strip().split()))
    s=list(map(lambda x:pow(x,n[-1]),l))
    print(lcm(s)%n[1])