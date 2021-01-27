#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    b=bin(n)[2:]
    m=re.finditer(r'((1){1,})',b)
    l=[]
    for i in m:
        l.append(len(list(i.groups())[0]))
    print(max(l))
