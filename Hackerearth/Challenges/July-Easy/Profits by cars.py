def Profit(N,P):
    sum=0
    for p in P:
        sum=sum+p
    return sum


if __name__=="__main__":
    T=int(input())
    for t in range(T):
        N=int(input())
        P=list(map(int,input().rstrip().split()))
        print(Profit(N,P))