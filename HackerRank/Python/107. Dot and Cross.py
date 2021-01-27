import numpy
def MatrixProduct(a,b):
    arr1=numpy.array(l1)
    arr2=numpy.array(l2)
    print(numpy.dot(arr1,arr2))
    #print(numpy.cross(arr1,arr2))

if __name__ == '__main__':
    N=int(input())
    l1=[]
    l2=[]
    for n in range(N):
        l1.append(list(map(int,input().split())))
    for m in range(N):
        l2.append(list(map(int,input().split())))
    MatrixProduct(l1,l2)



