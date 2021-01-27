def Anangrams(A,B):
    d1={}
    d2={}
    for i in range(len(A)):
        d1[A[i]]=A.count(A[i])
        d2[B[i]]=B.count(B[i])
    if d1==d2:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    A=input()
    B=input()
    Anangrams(A,B)