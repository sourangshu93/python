""" This programming is taking 2 Variable (integer) and swapping their value.
    a=a+b: new value of a is now assigned to a+b
    b=a-b: from a+b we are substracting the vaule of b and the result is assigned to b.
    a=a-b: from a+b we are substracting the value of b and the result is assigned to a.
    which is swapping the value of a and b
"""
if __name__=="__main__":
    a=int(input("Insert value of a:"))
    b=int(input("Insert value of b:"))
    a=a+b
    b=a-b
    a=a-b
    print("new value of a :",a)
    print("new value of b :",b)