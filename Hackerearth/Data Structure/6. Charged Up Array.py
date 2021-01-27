'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from itertools import combinations
def ChargedUpArray(N,A):
    m=[]
    for i in range(N+1):
        m=m+(list(map(set,combinations(A,i))))
    print(m)
    count=0
    sum=0
    for a in A:
        for j in m:

if __name__=="__main__":
    T=int(input())
    for t in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        ChargedUpArray(N,A)
