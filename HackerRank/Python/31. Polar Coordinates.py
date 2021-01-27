# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
import cmath
from cmath import phase
def PolarCoordinates(z):
    polar=list(cmath.polar(z))
    for pol in polar:
        print(pol)
if __name__=="__main__":
    z=complex(input())
    PolarCoordinates(z)