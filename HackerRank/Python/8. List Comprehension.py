if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list1=[x for x in range (0,n+1)]
    list2=[y for y in range (0,n+1)]
    list3=[z for z in range (0,n+1)]
    ar = []
    p=0
    for i in range (x+1):
        for j in range( y+1):
            for k in range (z+1):
                if i+j+k != n:
                    ar.append([])
                    ar[p]=[i,j,k]
                    p+=1
    print(ar)