# Write your code here
if __name__=="__main__":
    N,Q=input().split()
    a=list(map(str,input().split()))
    for q in range(int(Q)//2):
        b,c=input().split()
        a[int(c)-1]=b
        o,l,r=input().split()
        a1=(a[int(o)])+"".join(a[int(l):int(r)])
        a2=a1[::-1]
        s=0
        for i in range(len(a2)):
            s+=(int(a2[i]))*(2**i)
        if s%2==0:
            print("EVEN")
        else:
            print("ODD")