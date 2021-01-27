if __name__=="__main__":
    N=int(input())
    B=0
    l=[]
    for i in range(1,N+1):
        if B+i>N:
            break
        if (B+i)<=N:
            l.append(i)
            B=B+i
        if B+2*i>N:
            break
        if B+2*i<=N:
            l.append(2*i)
            B=B+2*i
    if (N-B)!=0:
        l.append((N-B))
    print(l)
    print(len(l))
    print(sum(l))
    if len(l)%2==0:
        print("Motu")
    else:
        print("Patlu")