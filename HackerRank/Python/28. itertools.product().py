# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys
import itertools
from itertools import product
#os.environ["OUTPUT_PATH"]="C:\\Users\\kundus6\\Desktop\\new.txt"
def Itertoolproduct(a,b):
    q=(list(product(a,b)))
    for i in q:
        print(i,end=" ")
if __name__ == '__main__':
    fptr=open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    result = Itertoolproduct(a,b)
    fptr.write(result+"\n")
    fptr.close()