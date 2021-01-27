# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == "__main__":
    s=str(input())
    k=str(input())
    pattern=re.compile(k)
    m=pattern.search(s)
    while not m:
        print("(-1, -1)")
        break
    while m:
        print ("({0}, {1})".format(m.start(), m.end() - 1))
        m = pattern.search(s,m.start() + 1)