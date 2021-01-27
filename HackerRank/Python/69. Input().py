# Enter your code here. Read input from STDIN. Print output to STDOU
    
if __name__ == '__main__':
    x,k = map(int, input().split())
    P=eval(input())
    if P==k:
        print("True")
    else:
        print("False")
