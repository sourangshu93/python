def BitwiseOr(A,B):
    sum=0
    for i in range(A,B+1):
        sum=sum+1
    if (A|B):
        print(sum+1)
    else:
        print(sum)

if __name__ == '__main__':
    A=int(input())
    B=int(input())
    BitwiseOr(A,B)