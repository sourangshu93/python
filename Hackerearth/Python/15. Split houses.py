if __name__=="__main__":
    n=int(input())
    l=input()
    m=l.replace(".","B")
    if "HH" in m:
        print("NO")
    else:
        print("YES")
        print(m)
