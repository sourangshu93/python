import sys
if __name__=="__main__":
    N,Q=input().strip().split()
    A=list(map(int,input().split()))
    for i in sys.stdin:
        L,R=input().strip().split()
        B=A[int(L)-1:(int(R))]
        print(sum(B)//(len(B)))