if __name__=="__main__":
    n=10000
    a=lambda x,y,z: x**3+y**3+z**3
    for i in range(1, n):
        t=(i//1000)
        h=(i-(1000*t))//100
        t=(i-(100*h))//10
        d=(i-(100*h)-(10*t))
        if a(h,t,d)==i:
            print(i,end=",")
