if __name__=="__main__":
    N,M=input().split()
    s=set()
    for m in range(int(M)):
        s=s.union(set(map(int,input().split())))
    print(len(s))