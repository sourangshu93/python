def arrow(n):
    width=n
    for i in range(n+1):
        print(((" * ")*i).ljust(width," "))
    for j in range(n-1,0,-1):
        print(((" * ")*j).ljust(width," "))

if __name__=="__main__":
    n=int(input())
    arrow(n)