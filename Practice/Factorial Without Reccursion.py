import os
import sys
import math
os.environ["OUTPUT_PATH"]="C:\\Users\\kundus6\\Desktop\\new.txt"
def factorial(n):
    l=1
    for i in range(n):
        l=l*(n-i)
    print(l)
        
if __name__ == '__main__':
    n=int(input())
    ftpr=open(os.environ["OUTPUT_PATH"],"w")
    result=factorial(n)
    ftpr.write(str(result))
    ftpr.close()