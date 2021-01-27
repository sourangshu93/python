if __name__=="__main__":
    N=int(input())
    a=[]
    for n in range(N):
        a.append(int(input()))
    d={}
    for i in a:
        d[i]=a.count(i)
    key_list=list(d.keys())
    value_list=list(d.values())
    print(key_list[value_list.index(max(value_list))])