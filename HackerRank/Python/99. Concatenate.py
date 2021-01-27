import numpy

def Concatenate(N,M,P):
    arr1=numpy.array(l1)
    arr2=numpy.array(l2)
    print(numpy.concatenate((arr1,arr2)))

if __name__ == '__main__':
    N,M,P=input().split()
    l1=[]
    l2=[]
    for n in range(int(N)):
        l1.append(list(map(int,input().split())))
    for m in range (int(M)):
        l2.append(list(map(int,input().split())))
    Concatenate(N,M,P)