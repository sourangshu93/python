import numpy

def arrays(arr):
    arr1=arr[::-1]
    return(numpy.array(arr1,float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
