#from list remove duplicate
def rmdups(li):
    l=[]
    for i in li:
        if i not in l:
            l.append(i)
    return l

if __name__ == '__main__':
    li=list(map(int,input().rstrip().split()))
    q=rmdups(li)
    print(q)