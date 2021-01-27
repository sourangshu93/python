# Write your code here
if __name__=="__main__":
    T=int(input())
    for t in range(T):
        c,n=input().strip().split()
        sum=0
        for i in range(1,int(n)+1):
            sum=sum+i
        print(int(c)%sum)