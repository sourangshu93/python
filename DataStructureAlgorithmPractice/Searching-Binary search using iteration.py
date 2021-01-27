''' Binary search the condition is the list has to be shorted and 
    first need to determine the mid point of the list and if the start index is less than end index
    mid point is determined if the mid element is greater than the key value then need to search 
    for that array in the lower indexes of the mid point. Else need to find in the upper indexes from
    the mid point.
    '''
def BinarySearch(A,key):
    start=0
    end=len(A)-1
    while start <= end:
        mid=(start+end)//2
        if key==A[mid]:
            print("True")
            break
        elif key<A[mid]:
            end=mid-1
        else: 
            start=mid+1
    else:
        print("False")

if __name__=="__main__":
    A=[10,24,33,46,57,88,90]
    key=int(input())
    BinarySearch(A,key)