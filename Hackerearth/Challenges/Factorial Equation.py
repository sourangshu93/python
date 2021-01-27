#HackerEarth Challange:Factorial equations
import math
def FactorialEquation(X,N):
    sol=int(X)**(math.factorial(int(N))%10)
    print(str(sol)[-1])
    
if __name__ == '__main__':
    X,N=input().split()
    FactorialEquation(X,N)