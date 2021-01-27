#Peterson number
import math
from math import factorial
if __name__=="__main__":
    n=1000
    for j in range(100,n):
        h=j//100
        t=(j-(100*h))//10
        d=(j-(100*h)-(10*t))
        if (factorial(h)+factorial(t)+factorial(d))==j:
            print(j)