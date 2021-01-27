# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def IsRegex(li):
    for j in li:
        try:
            re.compile(j)
            print("True")
        except re.error:
            print("False")
if __name__ == '__main__':
    N=int(input())
    li=[]
    for i in range(N):
        li.append(str(input()))
    IsRegex(li)