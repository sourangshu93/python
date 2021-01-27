if __name__=="__main__":
    N,Q=input().strip().split()
    arr=list(map(int,input().split()))
    new_arr=[]
    for i in range(1,int(N)+1):
        new_arr.append(sum(arr[0:i]))
    for j in range(int(Q)):
        l,r=input().strip().split()
        print((new_arr[int(r)-1]-new_arr[int(l)-1])//(int(r)-int(l)))