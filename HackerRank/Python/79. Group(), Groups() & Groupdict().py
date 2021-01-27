# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def RegexParsing(s):
    m=re.findall(r'(([a-zA-Z0-9])\2{1,})',s)
    if m:
        print((m[0])[-1])
    else:
        print(-1)
if __name__ == '__main__':
    s=str(input())
    RegexParsing(s)