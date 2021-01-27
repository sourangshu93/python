# Factorial using reccursion
def Factorial(n):
    if n==0:
        return 1
    else:
        return(n*Factorial(n-1))

if __name__=="__main__":
    n=int(input())
    f=Factorial(n)
    print(f)

# Fibonacii series using reccursion
def Fibonacii(n):
    if n<=1:
        return n
    else:
       return(Fibonacii(n-1)+Fibonacii(n-2))

n=int(input())
for i in range(n):
    print(Fibonacii(i),end=" ")
print()
# Print recusive
def RecSum(n):
    if n==0:
        return(0)
    else:
        return(n+RecSum(n-1))
n=int(input())
print(RecSum(n))
