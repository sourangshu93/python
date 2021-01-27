def Ladderophilia(N):
    width=5
    print(("*").ljust(4)+("*").rjust(1))
    for i in range(N):
        print(("*").ljust(4)+("*").rjust(1))
        print((("*")*width).center(width))
        print(("*").ljust(4)+("*").rjust(1))
    print(("*").ljust(4)+("*").rjust(1))
if __name__=="__main__":
    N=int(input())
    Ladderophilia(N)