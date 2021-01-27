#!/bin/python3
import math
import os
import random
import re
import sys
    
if __name__ == '__main__':
    N = int(input())
    li=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        domain=(emailID.split('@'))[-1]
        if re.fullmatch("[a-z@.]+",emailID) and len(emailID)<=50 and len(firstName)<=20 and re.fullmatch("[a-z]+",firstName) and domain=="gmail.com":
            li.append(firstName)
    li.sort()
    print(*li,sep="\n")
        