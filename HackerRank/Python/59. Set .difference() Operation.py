# Enter your code here. Read input from STDIN. Print output to STDOUT
def Difference(n1,e,n2,f):
    print(len(e.difference(f)))

if __name__ == '__main__':
    n1=int(input())
    e=set(map(int,input().split()))
    n2=int(input())
    f=set(map(int,input().split()))
    Difference(n1,e,n2,f)