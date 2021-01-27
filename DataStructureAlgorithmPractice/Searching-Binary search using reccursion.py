def BinarySearch(A,k,start,end):
    if start > end:
        return False
    else:
        mid=(start+end)//2
        if k==A[mid]:
            return True
        elif k < A[mid]:
            return(BinarySearch(A,k,start,mid-1))
        else:
            return(BinarySearch(A,k,mid+1,end))


if __name__=="__main__":
    A=[10,24,33,46,57,88,90]
    k=int(input())
    start=0
    end=len(A)-1
    f=BinarySearch(A,k,start,end)
    print(f)