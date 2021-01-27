#Hacker Earth: Number of divisors

def NoOfDivisor(n,k):
    sum=0
    for i in range(1,int(n)+1):
        if i%int(k)!=0:
            sum=sum+i
        if i%int(k)==0:
            def divn(i):
                p=i//int(k)
                if i%int(k)!=0:
                    return i
                else:
                    return divn(p)
            sum=sum+divn(i)
    print(sum)
if __name__ == '__main__':
    T=int(input())
    for t in range(T):
        n,k=input().split()
        NoOfDivisor(n,k)
    
