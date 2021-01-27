import numpy
def ZerosAndOnes(s):
    print(numpy.zeros(s, dtype = numpy.int))
    print(numpy.ones(s, dtype = numpy.int))

if __name__ == '__main__':
    s=tuple(map(int,input().split()))
    ZerosAndOnes(s)