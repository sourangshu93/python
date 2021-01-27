if __name__=="__main__":
    N=int(input())
    l=list(map(int,input().strip().split()))
    mul=1
    for n in range(N):
        mul=mul*l[n]
    print(mul%1000000007)