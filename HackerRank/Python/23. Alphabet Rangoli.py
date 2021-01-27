def print_rangoli(size):
    str="abcdefghijklmnopqrstuvwxyz"
    width=size*4-3
    #Top Portion
    for a in range(0,1):
        for b in range(a+1,size):
            a1=(str[size-b:size])
            a2=(str[size-b+1:size])[::-1]
            a3="-".join(a2+a1)
            print(a3.center(width,"-"))
    # Middle Portion
    l1=[]
    l2=[]
    for i in range(size):
        l1.append(str[i])
    for j in range(size-1,0,-1):
        l2.append(str[j])
    print(*(l2+l1),sep="-")
    #Bottom Portion
    for k in range(0,1):
        for l in range(k+1,size):
            s1=((str[l+1:size])[::-1])
            s2=(str[l:size])
            s="-".join(s1+s2)
            print(s.center(width,"-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)