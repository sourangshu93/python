# Enter your code here. Read input from STDIN. Print output to STDOUT
def SingleSubscription(s1,s2):
    s=s1.union(s2)
    print(len(list(s)))
if __name__ == '__main__':
    n=int(input())
    s1=set(map(int,input().split()))
    b=int(input())
    s2=set(map(int,input().split()))
    SingleSubscription(s1,s2)