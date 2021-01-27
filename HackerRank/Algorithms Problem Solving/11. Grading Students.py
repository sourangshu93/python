#!/bin/python3
import math
import os
import random
import re
import sys
def gradingStudents(grades):
    for i in grades:
        if ((i%5)!=0) and (((((i//5)+1)*5)-i)<3) and (i>37):
            j=((i//5)+1)*5
            print(j)
        if ((i%5)!=0) and (((((i//5)+1)*5)-i)>=3) and (i>37):
            print(i)
        if (i<=37) or ((i%5)==0):
            print(i)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()
