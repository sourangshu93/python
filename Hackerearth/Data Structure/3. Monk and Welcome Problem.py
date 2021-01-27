'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def ListSum(N,A,B):
    for i in range(N):
        print((A[i]+B[i]),end=" ")

if __name__=="__main__":
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    ListSum(N,A,B)