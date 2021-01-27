if __name__=="__main__":
    l,r,k=input().split()
    m=[]
    for i in range(int(l),int(r)+1):
        if i%int(k)==0:
            m.append(i)
    print(len(m))