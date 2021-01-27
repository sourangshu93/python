# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def FloatingPoint(T,s):
    t=re.findall('[.]',s)
    p=''.join(re.findall('\w',s))
    if (re.search("^[-,+,.,\d,]",s) or re.search('^[+,-][.]',s)) and re.search('[.]\d',s) and not re.search(r'(([+,-]){2,})',s) and len(t)==1 and p.isdigit() and not(re.search('\d[+,-]\d',s)):
        print("True")
    else:
        print("False")
    
if __name__ == '__main__':
    T=int(input())
    for i in range (T):
        s=(input())
        FloatingPoint(T,s)
#or re.search("^[-]",s)
#(len(t)==1) and (p.isdigit()=="True") and 