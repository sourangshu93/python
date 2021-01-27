from prettytable import PrettyTable
if __name__ == "__main__":
    T=int(input())
    for t in range(T):
        m,n=input().rstrip().split()
        l1=list(map(str,input().rstrip().split()))
        a=PrettyTable()
        a.field_names=l1
        for i in range(int(n)):
            a.add_row(list(map(str,input().rstrip().split())))
        print(a)