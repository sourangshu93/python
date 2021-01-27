if __name__=="__main__":
    T=int(input())
    for t in range(T):
        s1=sorted(list(input()))
        s2=sorted(list(input()))
        s3=s1.copy()
        for i in s3:
            if i in s1 and i in s2:
                s1.remove(i)
                s2.remove(i)
        print(len(s1)+len(s2))
        