# Enter your code here. Read input from STDIN. Print output to STDOUT
def SumOfSet(A):
    print(sum(list(A)))

if __name__ == '__main__':
    n=int(input())
    A=set(map(int,input().split()))
    N=int(input())
    for i in range(N):
        command=list(map(str,input().split()))
        if command[0]=="intersection_update":
            s1=set(map(int,input().split()))
            A.intersection_update(s1)
        if command[0]=="update":
            s2=set(map(int,input().split()))
            A.update(s2)
        if command[0]=="symmetric_difference_update":
            s3=set(map(int,input().split()))
            A.symmetric_difference_update(s3)
        if command[0]=="difference_update":
            s4=set(map(int,input().split()))
            A.difference_update(s4)
    SumOfSet(A)