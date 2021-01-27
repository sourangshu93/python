# Write your code here
def BubbleSort(N,A):
    count=0
    for i in range(N-1,0,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                tmp=A[j]
                A[j]=A[j+1]
                A[j+1]=tmp
                count+=1
    print((len(A)-1)-count)

if __name__=="__main__":
    N=int(input())
    A=list(map(int,input().strip().split()))
    BubbleSort(N,A)