if __name__=="__main__":
    T=int(input())
    for t in range(T):
        d=input()
        l=[]
        s1=''
        s2=''
        for i in d:
            if int(i)%2!=0:
                s1=s1+str(int(i)+1)
                s2=s2+str(int(i)-1)
        print(s1)
        print(s2)


