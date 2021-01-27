if __name__=="__main__":
    N=int(input())
    l=list(map(int,input().strip().split()))
    l1=list(set(l))
    l2=[]
    for i in range(l1[0],l1[-1]+1):
        l2.append(i)
    if l1==l2:
        print("YES")
    else:
        print("NO")