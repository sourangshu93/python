# Enter your code here. Read input from STDIN. Print output to STDOUT

def AverageMarks(N,X,l):
    q=list(zip(*l))
    print(q)
    dict={}
    for i,e in enumerate(q):
        dict[i]=(sum(list(e))/len(e))
    for key in dict:
        print(dict[key])
if __name__ == '__main__':
    N,X=input().split()
    l=[]
    for x in range(int(X)):
        l.append(list(map(float,input().split())))
    AverageMarks(N,X,l)