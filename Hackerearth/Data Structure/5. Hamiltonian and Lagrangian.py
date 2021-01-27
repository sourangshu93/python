'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def Hamiltonian(n,arr):
    l=[]
    l.append(arr[0])
    for i in range(n-1):
        if arr[i]<arr[i+1]:
           l.append(arr[i+1])
    print(*l[::-1])

if __name__=="__main__":
    n=int(input())
    arr=(list(map(int,input().split())))[::-1]
    Hamiltonian(n,arr)