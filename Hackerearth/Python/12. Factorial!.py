def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
if __name__=="__main__":
    n=int(input())
    a=Factorial(n)
    print(a)