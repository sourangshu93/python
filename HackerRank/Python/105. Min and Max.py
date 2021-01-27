import numpy
def MinMax(li):
    arr=numpy.array(li)
    arr1=numpy.min(arr,axis=1)
    print(numpy.max(arr1))

if __name__ == '__main__':
    N,M=input().split()
    li=[]
    for n in range(int(N)):
        li.append(list(map(int,input().split())))
    MinMax(li)