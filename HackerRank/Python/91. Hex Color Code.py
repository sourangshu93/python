# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    N=int(input())
    m=r'[\s|\S](#[0-9a-fA-F]{3,6})'
    l=[]
    for n in range(N):
        k=re.findall(m,input())
        for i in k:
            l.append(i)
    print(*l,sep="\n")

