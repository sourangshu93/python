# Write your code here
if __name__=="__main__":
    s=input()
    if s[-1]=='6':
        print(-1)
    else:
        s1=s.replace('6','')
        print(len(s1))