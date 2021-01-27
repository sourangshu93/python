def baloon(c,n,l):
    g=0
    p=0
    for i in range(len(l)):
        g=g+l[i][0]
        p=p+l[i][-1]
    print(g*c[0]+p*c[-1])
if __name__=="__main__":
    T=int(input())
    for t in range(T):
        if t%2==0:
            c=list(map(int,input().strip().split()))
            n=int(input())
            l=[]
            for i in range(n):
                l.append(list(map(int,input().strip().split())))
            baloon(c,n,l)
        if t%2!=0:
            c=list(map(int,input().strip().split()))[::-1]
            n=int(input())
            l=[]
            for i in range(n):
                l.append(list(map(int,input().strip().split())))
            baloon(c,n,l)

