def MinimumMoves(a):
    if a[0]<a[-1] :
        print(-1)
    else:
        print(a[0])

if __name__=="__main__":
    T=int(input())
    for t in range(T):
        a=list(map(int,input().rstrip().split()))
        MinimumMoves(a)