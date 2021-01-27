# Enter your code here. Read input from STDIN. Print output to STDOUT
def LetsReview(T,s):
    l1=[]
    l2=[]
    for i in range(len(s)):
        if i%2==0:
            l1.append(s[i])
        else:
            l2.append(s[i])
    print("".join(l1),end=" ")
    print("".join(l2))
if __name__=="__main__":
    T=int(input())
    for t in range (T):
        s=str(input())
        LetsReview(T,s)