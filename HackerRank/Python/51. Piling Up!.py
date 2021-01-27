# Enter your code here. Read input from STDIN. Print output to STDOUT
def PilingUp(n,s):
    for i in range (n//2):
        if (s[0]>=s[(-1)]) or (s[-1]>=s[(0)]) and ((s[0]>=s[1]) or(s[-1]>=s[-2])):
            s.pop(0)
            s.pop(-1)
    if len(s)==0 or len(s)==1: #If the no of element is odd then the last element will remain in the list after pop opration
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    T=int(input())
    for t in range(T):
        n=int(input())
        s=list(map(int,input().split()))
        PilingUp(n,s)