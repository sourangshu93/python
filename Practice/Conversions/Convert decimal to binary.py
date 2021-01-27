""" This program converts decimal number to binary number.
    This is written using normal method.
    Not using reccursion function.
"""
def DecomalToBin(a):
    l=[]
    if a==0:
        print(0)
    else:
        for i in range(a//2):
            l.append(str(a%2))
            a=a//2
            if a==1:
                l.append("1")
                break   
    print("The binary value of",a,"is:","".join(l[::-1]))

if __name__=="__main__":
    a=int(input("Enter a decimal no: "))
    DecomalToBin(a)