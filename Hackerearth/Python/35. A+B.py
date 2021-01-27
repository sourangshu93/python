import sys
if __name__=="__main__":
    l1=[]
    for i in sys.stdin:
        l=list(map(int,i.split()))
        l1.append(sum(l))
    print(*l1,sep="\n")