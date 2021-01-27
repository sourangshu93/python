# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
from math import pow
def MaximizeIt(K,M,l):
    l1=[]
    q=list(set(product(*l)))
    for i in q:
        l1.append((sum(list(map(lambda j : j**2, list(i))))) % (int(M)))
    print(max(l1))
if __name__=="__main__":
    K,M=(input().split())
    l=[]
    for k in range(int(K)):
        w=list(map(int,input().split()))
        l.append(w[1:])
    MaximizeIt(K,M,l)