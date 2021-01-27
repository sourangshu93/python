# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#def ValidNo(N,s):
    
if __name__ == '__main__':
    N=int(input())
    for i in range(N):
        try:
            s=str(input())
            m=re.search(r'[7-9]+', s)
            if len(s)==10 and m.start()==0 and s.isdigit():
                print("YES")
            else:
                print("NO")
        except AttributeError:
            print("NO")