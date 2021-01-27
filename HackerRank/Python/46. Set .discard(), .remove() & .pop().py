def SetOperations(n,s,N):
    l1=list(s)
    print(sum(l1))
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for i in range(N):
        command=(input().split())
        if command[0]=="pop":
            s.pop()
        if command[0]=="remove":
            s.remove(int(command[-1]))
        if command[0]=="discard":
            s.discard(int(command[-1]))
    SetOperations(n,s,N)