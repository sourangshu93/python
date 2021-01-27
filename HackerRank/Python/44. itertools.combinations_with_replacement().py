# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
def CombinationWithReplacement(s):
    st=s[0]
    r=int(s[-1])
    li=[]
    for i in st:
        li.append(i)
        li.sort()
    l=list(combinations_with_replacement(li,r))
    for j in l:
        print("".join(j))
if __name__ == '__main__':
    s=list(map(str,input().split()))
    CombinationWithReplacement(s)