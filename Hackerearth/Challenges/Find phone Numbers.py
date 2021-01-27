import re
def PhoneNumbers(P):
    q=(re.findall(r'(\d\d\d-\d\d\d-\d\d\d\d)*',P))
    d={}
    for i in range(len(q)):
        d[q[i]]=q.count(q[i])
    print(d)
    print(max(d))

if __name__=="__main__":
    P=input()
    PhoneNumbers(P)