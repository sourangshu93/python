# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
def Probablity(N,s,K):
    li=(list(combinations(s,K)))
    count=0
    for i in li:
        if "a" in i:
            count+=1
    print(count/len(li))
if __name__ == '__main__':
    N=int(input())
    s=list(map(str,input().split()))
    K=int(input())
    Probablity(N,s,K)