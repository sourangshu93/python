d={"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
if __name__=="__main__":
    T=int(input())
    for t in range(T):
        s=input()
        a=0
        for i in s:
            a=a+(d[i])
        if a%2==0 or a < 3:
            print("1"*(a//2))
        if a >= 3 and a%2!=0:
            print(("7")+("1"*((a-3)//2)))

        