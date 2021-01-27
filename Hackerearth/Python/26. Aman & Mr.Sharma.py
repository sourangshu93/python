if __name__=="__main__":
    D=int(input())
    s=0
    for d in range(D):
        r,x=input().rstrip().split()
        perimeter=(44*int(r))/7
        h = 100*int(x)
        if h >=perimeter:
            s+=1
    print(s)
