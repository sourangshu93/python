# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def OrderDictionary(orders,l1):
    for key in orders:
        c=(l1.count(key))
        print(key,end=" ")
        print(orders[key]*c)
if __name__ == '__main__':
    N=int(input())
    orders={}
    l1=[]
    for i in range(N):
        a=list(input().split())
        k1=a[0:-1]
        k=" ".join(k1)
        v=int(a[-1])
        orders[k]=v
        l1.append(k)
    OrderDictionary(orders,l1)