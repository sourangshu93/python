def pattern(n):
    width=2*n
    for i in range(2*n-2,-1,-2):
        print((("#")*i).center(width,"*"))

if __name__=="__main__":
    T=int(input())
    for t in range(T):
        N=int(input())
        pattern(N)