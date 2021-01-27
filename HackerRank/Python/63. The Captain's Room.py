# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
def CaptainRoom(n,l):
    s1=set(l)
    s2=set([item for item, count in collections.Counter(l).items() if count > 1])
    l1=(list(s1.symmetric_difference(s2)))
    for i in l1:
        print(i)
if __name__ == '__main__':
    n=int(input())
    l=list(map(int,input().split()))
    CaptainRoom(n,l)