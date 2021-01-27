import string
def CharSum(S):
    a=string.ascii_lowercase
    s=0
    for i in S:
        s+=(int(a.index(i))+1)
    print(s)
if __name__ == "__main__":
    S=input()
    CharSum(S)