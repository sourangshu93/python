def digit_sum(x):
    sum=0
    Y=str(x)
    for y in Y:
        sum=sum+int(y)
    return(sum)
def lowestIndex(N,Q,A,p):
    ith_ele=A[p-1]
    jth_ele=A[p]
    if jth_ele > ith_ele and digit_sum(A[p-1])> digit_sum(A[p]):
        print(p+1)
    else:
        print(-1)
        
if __name__=="__main__":
    N,Q=input().rstrip().split()
    A=list(map(int,input().rstrip().split()))
    for q in range(int(Q)):
        p=int(input())
        try:
            lowestIndex(N,Q,A,p)
        except IndexError:
            print(-1)