def BinarytoDecimal(n):
    sum=0
    s1=n[::-1]
    for i in range(len(s1)):
        sum=sum+(int(s1[i])*2**i)
    print("The decimal value of",n,"is",sum)
if __name__=="__main__":
    n=input("Input a Binary Number: ")
    BinarytoDecimal(n)