# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def Combinations(s):
    st=s[0]
    r=int(s[-1])
    li=[]
    for i in st:
        li.append(i)
        li.sort()
    for p in range (1,r+1):
        d=list(combinations(li,p))
        for j in d:
            print(''.join(j))
if __name__ == '__main__':
    s=list(map(str,input().split()))
    Combinations(s)