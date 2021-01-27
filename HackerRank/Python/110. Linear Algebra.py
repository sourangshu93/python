from numpy import linalg

def LinearAlgebra(N,l):
    det=linalg.det(l)
    s=str(det).split('.')
    if (len(s[-1]))>1:
        print("{:.2f}".format(det))
    else:
        print(det)

if __name__ == '__main__':
    N=int(input())
    l=[]
    for n in range(N):
        l.append(list(map(float,input().split())))
    LinearAlgebra(N,l)