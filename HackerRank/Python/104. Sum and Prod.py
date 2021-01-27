import numpy
def SumProduct(l1):
    arr=numpy.array(l1)
    arr1=numpy.sum(arr, axis=0)
    print(numpy.prod(arr1))

if __name__=="__main__":
    N,M=input().split()
    l1=[]
    for n in range(int(N)):
        l1.append(list(map(int,input().split())))
    SumProduct(l1)