if __name__=="__main__":
    M=int(input())
    A=list(map(int,input().rstrip().split()))
    d={}
    for i in A:
        d[i]=A.index(i)
    print(*(dict(sorted(d.items()))).values())