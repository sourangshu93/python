# Enter your code here. Read input from STDIN. Print output to STDOUT
def SymmetricDiffrence(n1,e,n2,f):
    print(len(e.symmetric_difference(f)))
    
if __name__ == '__main__':
    n1=int(input())
    e=set(map(int,input().split()))
    n2=int(input())
    f=set(map(int,input().split()))
    SymmetricDiffrence(n1,e,n2,f)