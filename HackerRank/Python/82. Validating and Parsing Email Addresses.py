# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        try:
            s=str(input())
            q=email.utils.parseaddr(s)
            r=email.utils.formataddr(q)
            t=email.utils.parseaddr(r)
            username=(q[-1].split("@"))[0]
            domain=(((q[-1]).replace(".","@")).split("@"))[-2]
            extension=(((q[-1]).replace(".","@")).split("@"))[-1]
            l=((q[-1].split("@"))[1]).split(".")
            if username.replace("-","").replace("_","").replace(".","").isalnum() and username[0].isalpha() and q[-1]==(email.utils.parseaddr(r))[-1] and domain.isalpha() and extension.isalpha() and (1<=len(extension)<=3) and (len(l)==2):
                print(r)
        except IndexError:
            pass