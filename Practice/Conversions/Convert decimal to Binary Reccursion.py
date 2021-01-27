""" This program converts decimal value to binary using reccursion.
    Incomplete
"""
def BinaryConvert(d):
    l=[]
    if d==0:
        l.append(0)
        print(l)
    if d==1:
        l.append(1)
        print(l)
    if d==2:
        l.append(d%2)
        print(l)
    else:
        l.append(BinaryConvert(d%2))
        l.append(2)
        print(l)
    

if __name__=="__main__":
    n=int(input("Enter a decimal no:"))
    BinaryConvert(n)