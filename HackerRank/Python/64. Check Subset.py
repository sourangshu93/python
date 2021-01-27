# Enter your code here. Read input from STDIN. Print output to STDOUT
def SubsetCheck(a,A,b,B):
    if A.issubset(B):
        print("True")
    else:
        print("False")
if __name__ == '__main__':
    T=int(input())
    for t in range(T):
        a=int(input())
        A=set(map(int,input().split()))
        b=int(input())
        B=set(map(int,input().split()))
    SubsetCheck(a,A,b,B)