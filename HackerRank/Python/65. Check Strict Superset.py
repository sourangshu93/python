# Enter your code here. Read input from STDIN. Print output to STDOUT
li=[]
if __name__ == '__main__':
    A=set(map(int,input().split()))
    N=int(input())
    for n in range(N):
        B=set(map(int,input().split()))
        if A.issuperset(B):
            li.append("True")
        else:
            li.append("False")
    if "False" in li:
        print("False")
    else:
        print("True")
        