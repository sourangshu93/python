import numpy
def transpose(p):
    q=numpy.array(p)
    print(numpy.transpose(q))
    print(q.flatten())

if __name__ == '__main__':
    n,m=input().split()
    p=[]
    for i in range(int(n)):
        p.append(list(map(int,input().split())))
    transpose(p)