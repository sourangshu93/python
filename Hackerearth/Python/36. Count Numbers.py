import re 
if __name__=="__main__":
    T=int(input())
    for t in range(T):
        N=int(input())
        s=input()
        l=re.findall(r'\d{1,}',s)
        print(len(l))