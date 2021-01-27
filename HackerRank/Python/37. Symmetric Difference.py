# Enter your code here. Read input from STDIN. Print output to STDOUT

def SymmetricDifference(l1,l2):
    s1=set(l1)
    s2=set(l2)
    s3=s1.union(s2)-s1.intersection(s2)
    l3=list(s3)
    l3.sort()
    for i in l3:
        print(i)
if __name__ == '__main__':
    M=int(input())
    l1=list(map(int,input().split()))
    N=int(input())
    l2=list(map(int,input().split()))
    SymmetricDifference(l1,l2)
    # 2 4 5 9
    # 2 4 11 12