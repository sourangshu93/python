import string
l=string.ascii_lowercase
def Neutral(s):
    if len(s)==0:
        return
    if len(s)==1:
        return s
    else:
        for i in l:
            s1=Neutral(s1).replace(i*2,"")
        return s1
    
if __name__=="__main__":
    N=int(input())
    s=input()
    print(Neutral(s))
