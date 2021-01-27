# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
def CompressedString(s):
    q=groupby(s)
    tup=()
    for i,j in q:
        l=list(j)
        tup=(l.count(i),int(i))
        print(tup,end=" ")
if __name__ == '__main__':
    s=str(input())
    CompressedString(s)
