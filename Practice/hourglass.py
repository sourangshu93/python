def Hourglass(n):
    
    if n%2!=0:
        width1=n
        for i in range(n,1,-2):
            print((("*")*i).center(width1," "))
        for i in range(1,n+1,2):
            print((("*")*i).center(width1," "))
    if n%2==0:
        width2=n+1
        for i in range(n,1,-2):
            print((("*")*i).center(width2," "))
        print(("*").center(width2," "))
        for i in range(2,n+1,2):
            print((("*")*i).center(width2," "))
if __name__=="__main__":
    n=int(input("Enter an integer: "))
    Hourglass(n)