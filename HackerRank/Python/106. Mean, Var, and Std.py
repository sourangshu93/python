import numpy

def MeanVarStd(l1):
    arr=numpy.array(l1)
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(numpy.std(arr))

if __name__ == '__main__':
    N,M=input().split()
    l1=[]
    for n in range(int(N)):
        l1.append(list(map(int,input().split())))
    MeanVarStd(l1)