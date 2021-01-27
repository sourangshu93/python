'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def rotRight(a, d):
    l1=[]
    if d==0:
        return a
    if d==1:
        l1.append(a[-1])
        for i in range(len(a)-1):
            l1.append(a[i])
        return(l1)
    else:
        return(rotRight(rotRight(a,1),d-1))
if __name__ == '__main__':
    n = int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    d=int(input())
    result=rotRight(a,d)
    print(*result,sep="\n")