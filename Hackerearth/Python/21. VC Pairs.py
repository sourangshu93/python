if __name__=="__main__":
    T=int(input())
    for t in range(T):
        N=int(input())
        S=input()
        c=0
        for i in range(N):
            if S[i] not in ['a','e','i','o','u'] and S[i-1] in ['a','e','i','o','u']:
                c=c+1
        print(c)

