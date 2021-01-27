# Write your code here
def Polynomial(a,b,c):
    sum=0
    for i in range (len(A)):
        e=lambda x: x**A[i]
        
    if a=="0":
        A[int(b)-1]= int(c)
    if a=="1":
        if e(int(b))==int(c):
            print("Yes")
        else:
            print("No")

if __name__=="__main__":
    N,Q=input().split()
    A=list(map(int,input().split()))
    for q in range(int(Q)):
        a,b,c=input().split()
        Polynomial(a,b,c)
