'''
    In linear search the iteration starts from the start of the list and traverses all the elements
    and if the key is found in the list/array then if the key matches the result shows true otherwise returns false
    '''
def linearsearch(A,key):
    for i in (A):
        if i==key:
            print("True")
            break
    else:
        print('False')

if __name__=="__main__":
    A=[10,34,22,9,28,88]
    key=int(input())
    linearsearch(A,key)