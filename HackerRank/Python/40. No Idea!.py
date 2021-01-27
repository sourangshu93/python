# Enter your code here. Read input from STDIN. Print output to STDOUT

def Happiness(n,m,s,A,B):
    print (sum([(i in A) - (i in B) for i in s]))

if __name__ == '__main__':
    n,m=list(map(int,input().split()))
    s=list(map(int,input().split()))
    A=set(map(int,input().split()))
    B=set(map(int,input().split()))
    Happiness(n,m,s,A,B)