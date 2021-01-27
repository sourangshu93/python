if __name__=="__main__":
    T=int(input())
    for t in range(T):
        a,b=input().split()
        if sorted(a)==sorted(b):
            print("YES")
        else:
            print("NO")