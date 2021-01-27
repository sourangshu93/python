# Enter your code here. Read input from STDIN. Print output to STDOUT
def ModDivmod(d,a):
    print(d//a)
    print(d%a)
    print(divmod(d,a))
if __name__=="__main__":
    d=int(input())
    a=int(input())
    ModDivmod(d,a)