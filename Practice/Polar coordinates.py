# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
import math
import cmath
from cmath import phase
def PolarCoordinates(z):
    x=z.real
    y=z.imag
    print(math.sqrt(x**2+y**2))
    print(math.atan(y/x))
if __name__ == '__main__':
    z=complex(input("Enter a complex number z:"))
    PolarCoordinates(z)