def MulOccu(A,N):
    sum=0
    B=list(set(A))
    C=A[::-1]
    for b in B:
        ind1=A.index(b)
        ind2=C.index(b)
        sum=sum+




if __name__=="__main__":
    T=int(input())
    N=int(input())
    A=list(map(int,input().rstrip().split()))
    for t in range(T):
        MulOccu(A,N)