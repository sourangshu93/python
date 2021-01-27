# Enter your code here. Read input from STDIN. Print output to STDOUT
def Intersection(n,s1,b,s2):
    print(len(s1.intersection(s2)))
if __name__ == '__main__':
    n=int(input())
    s1=set(map(int,input().split()))
    b=int(input())
    s2=set(map(int,input().split()))
    Intersection(n,s1,b,s2)