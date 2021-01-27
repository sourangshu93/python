import numpy
def floor(n):
    numpy.set_printoptions(legacy='1.13')
    print(numpy.floor(n),numpy.ceil(n),numpy.rint(n),sep="\n")

if __name__ == '__main__':
    n=numpy.array(list(map(float,input().split())))
    floor(n)