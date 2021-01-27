def Neutralisation(n,s):
    for i in range(n):
        if s[i]!=s[i+1]:
            return(s)
        if s[i]==s[i+1]:
            s1=s.replace(s[i],"").replace(s[i+1],"")
            return(s1)
        else:
            return(Neutralisation(n-2,s1))


if __name__=="__main__":
    n=int(input())
    s=input()
    result=Neutralisation(n,s)
    print(result)