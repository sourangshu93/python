# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N=input()
    l=list(map(int,input().split()))
    print(all(i>=0 for i in l) and any(str(i)==str(i)[::-1] for i in l))