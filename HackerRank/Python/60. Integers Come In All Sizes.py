# Enter your code here. Read input from STDIN. Print output to STDOUT
def LargeIntegers(a,b,c,d):
    q=(int(a**b)+int(c**d))
    print("{}".format(q))
if __name__ == '__main__':
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    LargeIntegers(a,b,c,d)