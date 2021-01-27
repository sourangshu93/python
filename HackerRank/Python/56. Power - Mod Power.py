# Enter your code here. Read input from STDIN. Print output to STDOUT
def PowerModPower(a,b,m):
    r=a**b
    print(r)
    print(r%m)
    
if __name__ == '__main__':
    a=int(input())
    b=int(input())
    m=int(input())
    PowerModPower(a,b,m)