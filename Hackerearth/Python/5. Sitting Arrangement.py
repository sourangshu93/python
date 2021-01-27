if __name__=="__main__":
    T=int(input())
    for t in range(T):
        s=int(input())
        d=s//12
        r=s%12
        if r == 0:
            opposite_sit=(12*(d-1))+1
        else:
            opposite_sit=(12*d)+(13-r)
        if s%6==0 or s%6==1:
            print("{} {}".format(opposite_sit,"WS"))
        if s%6==2 or s%6==5:
            print("{} {}".format(opposite_sit,"MS"))
        if s%6==3 or s%6==4:
            print("{} {}".format(opposite_sit,"AS"))