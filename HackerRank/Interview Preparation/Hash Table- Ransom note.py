#!/bin/python3
import math
import os
import random
import re
import sys
import builtins
from builtins import hash
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    print(list(map(hash, magazine)))
    print(hash(1))
        
if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
