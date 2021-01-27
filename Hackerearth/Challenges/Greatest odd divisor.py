if __name__=="__main__":
    T=int(input())
    for t in range (T):
        n,m=input().split()
        sum=0
        for i in range(1,int(n)):
            if (int(n)//i)%2!=0:
                sum=sum+(int(n)//i)
        print(sum%int(m)