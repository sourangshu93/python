# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
def CollectionsDeque(N,c):
    for j in d:
        print(j,end=" ")
    
if __name__ == '__main__':
    N=int(input())
    d=deque()
    for i in range(N):
        c=input().split()
        if c[0]=="append":
            d.append(int(c[-1]))
        if c[0]=="appendleft":
            d.appendleft(int(c[-1]))
        if c[0]=="pop":
            d.pop()
        if c[0]=="popleft":
            d.popleft()
    CollectionsDeque(N,c)