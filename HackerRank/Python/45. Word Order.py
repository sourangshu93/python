# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
def WordOrder(d):
    print(len(d))
    for key in d:
        print((sum(d[key])),end=" ")
if __name__ == '__main__':
    n=int(input())
    d=defaultdict(list)
    for i in range(n):
        d[str(input())].append(1)
    WordOrder(d)