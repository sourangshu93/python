arr=[]
if __name__ == '__main__':
    for n in range(int(input())):
        name = input()
        score = float(input())
        arr.insert(n,[name,score])
        n=n+1
    arr.sort(key=lambda x:x[1])
    arr.reverse()
    q=(arr[-1])
    r=(q[-1])
    count=0
    for a,b in arr:
        if b==r:
            count+=1
    s=(arr[-1-count])
    t=(s[-1])
    for c,d in arr:
        if d==t:
            print(c)