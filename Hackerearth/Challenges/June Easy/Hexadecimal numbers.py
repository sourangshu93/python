def HexNumbers(s):
    l=[]
    for i in range(int(s[0]),int(s[-1])+1):
        if i > 1:
            l.append(i)
    print(len(l))


if __name__=="__main__":
    T=int(input())
    for t in range(T):
        s=input().split()
        HexNumbers(s)