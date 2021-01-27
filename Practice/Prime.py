# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def PrimeNumber(n):
    q=round(math.sqrt(n))
    if 2<=n<1000:
        for i in range(2,n):
            if n%i==0 :
                print("Not prime")
                break
        else:
            print("Prime")
    if n>=1000:
        for j in range(2,q):
            if n%j==0 :
                print("Not prime")
                break
        else:
            print("Prime")
    if n<2:
        print("Not Prime")
if __name__=="__main__":
    N=int(input())
    for j in range(N):
        n=int(input())
        PrimeNumber(n)