def Pyramid(n):
    width=n
    for i in range(1,n,2):
        print((("*")*i).center(width," "))
        
if __name__=="__main__":
    n=int(input("Enter the pyramid height: "))
    Pyramid(n)
    