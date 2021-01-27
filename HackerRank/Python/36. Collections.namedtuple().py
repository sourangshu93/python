# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
from collections import namedtuple
def NamedTuple(marks):
    print(sum(marks)/len(marks))
if __name__ == '__main__':
    (n, categories) = (int(input()), input().split())
    Grade = namedtuple('Grade', categories)
    marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
    NamedTuple(marks)

