import numpy
def Reshape(n):
    m=numpy.array(n)
    print(numpy.reshape(m,(3,3)))

if __name__ == '__main__':
    n=list(map(int,input().strip().split()))
    Reshape(n)
    