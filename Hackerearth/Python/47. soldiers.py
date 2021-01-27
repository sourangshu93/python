if __name__=="__main__":
    N=int(input())
    S=list(map(int,input().rstrip().split()))
    Q=int(input())
    for q in range(Q):
        count=0
        a=0
        M=int(input())
        for s in S:
            if s<= M:
                count=count+1
                a=a+s
        print(count,a)