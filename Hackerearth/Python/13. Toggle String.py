if __name__=="__main__":
    S=input()
    l=[]
    for i in S:
        if i.isupper():
            l.append(i.lower())
        if i.islower():
            l.append(i.upper())
    print("".join(l))
