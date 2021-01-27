import upsidedown
def IsSrtoboGramaticNumber(n):
    p=str(n)
    for i in range (0,len(n)):
        if (p[i]=="6"):
            r=p.replace(str(p[i]),"9")
        if (p[i]=="9"):
            
if __name__ == '__main__':
    n=input()
    q=IsSrtoboGramaticNumber(n)
    print(q)