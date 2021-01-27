import re
import sys
import os
os.environ["OS_PATH"]="C:\\Users\\kundus6\\Desktop\\new.txt"
if __name__ == '__main__':
    fptr=open(os.environ['OS_PATH'], 'w')
    N=int(input())
    s=sys.stdin.read()
    s=(re.sub(r"\s&&(?=\s)"," and",s))
    s=(re.sub(r"\s\|\|(?=\s)"," or",s))
    print(s)
    fptr.write(s+"\n")
    fptr.close()