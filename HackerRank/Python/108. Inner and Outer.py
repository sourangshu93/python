import numpy

def InnerOuter(a,b):
    arr1=numpy.array(a)
    arr2=numpy.array(b)
    print(numpy.inner(arr1,arr2))
    print(numpy.outer(arr1,arr2))

if __name__ == '__main__':
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    InnerOuter(a,b)