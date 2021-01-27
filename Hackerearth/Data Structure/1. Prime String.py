import multiprocessing
def isPrime(a):
    if a==1:
        return(bool(0))
    else:
        for b in range(2,a):
            if a%b==0:
                return(bool(0))
                break
        else:
            return(bool(1))
def IsPrimeString(N,s):
    d={}
    for j in s:
        d[j]=s.count(j)
    l1=[]
    for k in d.values():
        l1.append(bool(isPrime(k)))
    if isPrime(len(d)) and all(l1):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    N=int(input())
    for n in range(N):
        s=str(input())
        print(result)
