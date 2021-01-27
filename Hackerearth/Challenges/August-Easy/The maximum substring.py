import re
if __name__=="__main__":
    s=input()
    m=re.findall(r'^([a-z]{2,}?)\1+',s)
    #m=re.findall(r'(.{1,})\1',s)
    print(m[0])