# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def ValidateCreditCard(N,s):
    m=s.replace('-',"")
    try:
        t=re.findall('\w+',s)
        if re.search(r'^[4-6]',s) and len(m)==16 and m.isdigit() and (len(t[0])==len(t[1])==len(t[2])==len(t[3])==4) and not re.search(r'((\d)\2{3,})',m) and len("".join(re.findall("\W+",s)))==3:
            print("Valid")
        else:
            print("Invalid")
    except IndexError:
        t=re.findall("\d\d\d\d",s)
        if re.search(r'^[4-6]',s) and len(m)==16 and m.isdigit() and (len(t[0])==len(t[1])==len(t[2])==len(t[3])==4) and not re.search(r'((\d)\2{3,})',m):
            print("Valid")
        else:
            print("Invalid")


if __name__ == '__main__':
    N=int(input())
    for n in range(N):
        s=input()
        ValidateCreditCard(N,s)
