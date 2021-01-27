'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def ArrayUpdate(N,K,A):
    count=0
    min_value=min(A)
    while min_value < int(K):
        count=count+1
        min_value=min_value+1
    print(count)
if __name__=="__main__":
    T=int(input())
    for t in range(T):
        N,K=input().split()
        A=list(map(int,input().split()))
        ArrayUpdate(N,K,A)
