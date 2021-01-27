import string
def Cipher(S,N):
    au=string.ascii_uppercase
    al=string.ascii_lowercase
    an=string.digits
    asy=string.punctuation
    l=[]
    for i in S:
        if i in au:
            ind1 = au.index(i)
            if ind1+N > len(au)-1:
                l.append(au[N-(len(au)-ind1)])
            else:
                l.append(au[ind1+N])
        if i in al:
            ind2 = al.index(i)
            if ind2+N > len(al)-1:
                l.append(al[N-(len(al)-ind2)])
            else:
                l.append(al[ind2+N])
        if i in an:
            ind3 = an.index(i)
            if ind3+N > len(an)-1:
                l.append(an[N-(len(an)-ind3)])
            else:
                l.append(an[ind3+N])
        if i in asy:
            l.append(i)
    print("".join(l))
if __name__=="__main__":
    S=input()
    N=int(input())
    if N > 26:
        A=N%26
        Cipher(S,A)
    else:
        Cipher(S,N)
