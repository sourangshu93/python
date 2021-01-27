def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b
        i=i+1
if __name__=="__main__":
    n=int(input())
    fib(n)