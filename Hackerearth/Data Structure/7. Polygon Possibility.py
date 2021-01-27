def Polygon(n,li):
    max_side=max(li)
    sum_list=sum(li)
    if (sum_list-max_side)>max_side:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    T=int(input())
    for t in range(T):
        n=int(input())
        li=list(map(int,input().split()))
        Polygon(n,li)