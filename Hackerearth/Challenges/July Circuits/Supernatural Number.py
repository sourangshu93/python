if __name__=="__main__":
    n=int(input())
    l=[]
    for i in range(2,n+1):
        if i*i==n:
            l.append(i)
        elif i==n:
            l.append(i)
    print(len(l))