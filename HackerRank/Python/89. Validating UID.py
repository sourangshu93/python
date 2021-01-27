# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def ValidUID(T,s):
    st="".join(re.findall('\D+',s))
    l1=[]
    for i in st:
        if i.isupper():
            l1.append(i)
    
    num="".join(re.findall('\d+',s))
    if s.isalnum() and len(s)==10 and len(l1)>=2 and len(set(num))>=3 and len(st)==len(set(st)) and len(num)==len(set(num)):
        print("Valid")
    else:
        print("Invalid")
if __name__ == '__main__':
    T=int(input())
    for t in range(T):
        s=str(input())
        ValidUID(T,s)