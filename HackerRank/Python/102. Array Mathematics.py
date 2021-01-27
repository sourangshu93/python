import numpy
def ArrayMathematics(l1,l2):
    A=numpy.array((l1))
    B=numpy.array((l2))
    numpy.set_printoptions(legacy='1.13')
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)
    print(A**B)

if __name__ == '__main__':
    N,M=input().split()
    l1=[]
    l2=[]
    for i in range (int(N)):
        l1.append(list(map(int,input().split())))
    for i in range (int(N)):
        l2.append(list(map(int,input().split())))
    ArrayMathematics(l1,l2)