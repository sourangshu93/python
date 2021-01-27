# Enter your code here. Read input from STDIN. Print output to STDOUT
def Exceptions(li):
    for i in li:
        try:
            print(int(i[0])//int(i[1]))
        except (ZeroDivisionError,ValueError,SyntaxError) as e:
            print("Error Code:",e)
if __name__ == '__main__':
    N=int(input())
    li=[]
    for n in range(N):
        l=list(map(str,input().split()))
        li.append(l)
    Exceptions(li)