# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator
import string
def ginortS(S):
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in S:
        if i in string.ascii_lowercase:
            l1.append(i)
        if i in string.ascii_uppercase:
            l2.append(i)
        if i in string.digits:
            if int(i)%2!=0:
                l3.append(i)
            if int(i)%2==0:
                l4.append(i)
    l1.sort()
    l2.sort()
    l3.sort()
    l4.sort()
    l=(l1+l2+l3+l4)
    for e in l:
        print(e,end="")
if __name__ == '__main__':
    S=str(input())
    ginortS(S)