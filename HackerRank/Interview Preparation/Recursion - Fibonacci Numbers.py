def fibonacci(n):
    if n==0:
        return n
    if n==1:
        return n
    else:
        for i in range(n):
            return(fibonacci(n-1)+fibonacci(n-2))

n = int(input())
print(fibonacci(n))