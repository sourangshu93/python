import re
if __name__ == "__main__":
    s=input()
    s1=s.replace('-',"")
    w="".join(re.findall("[A-Z]",s1))
    s2=s1.replace(w,"")
    if (int(s2[0])+int(s2[1]))%2==0 and (int(s2[2])+int(s2[3]))%2==0 and (int(s2[3])+int(s2[4]))%2==0 and (int(s2[5])+int(s2[6]))%2==0 and (w not in "AEIOUY"):
        print("valid")
    else:
        print("invalid")