import numpy
def Polinomials(P,x):
    print(numpy.polyval(P,x))
    
if __name__=="__main__":
    P=list(map(float,input().split()))
    x=int(input())
    Polinomials(P,x)