# Write your code here
if __name__=="__main__":
    s=input()
    b=str()
    for i in range(len(s)):
        while s[i]==s[i-1]:
            b+=s[i-1]
    print(len(b))