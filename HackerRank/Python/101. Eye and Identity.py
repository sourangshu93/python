import numpy

def EyeIdentity(n,m):
    if int(n)==int(m):
        arr1=(numpy.eye(int(n),int(m),k=0))
        numpy.set_printoptions(legacy='1.13')
        print(arr1)
    if n!=m:
        arr2=(numpy.eye(int(n),int(m),k=0))
        numpy.set_printoptions(legacy='1.13')
        print(arr2)
if __name__ == '__main__':
    n,m=input().split()
    EyeIdentity(n,m)