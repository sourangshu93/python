# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def FindMatch(s):
    if re.findall('([^a,e,i,o,u,A,E,I,O,U])([a,e,i,o,u,A,E,I,O,U]{2,})(?=[^a,e,i,o,u,A,E,I,O,U])',s):
        l=re.findall('[^a,e,i,o,u,A,E,I,O,U]([a,e,i,o,u,A,E,I,O,U]{2,})(?=[^a,e,i,o,u,A,E,I,O,U])',s)
        print(*l,sep="\n")
    else:
        print("-1")

if __name__ == '__main__':
    s=str(input())
    FindMatch(s)