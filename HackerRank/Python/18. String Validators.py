if __name__ == '__main__':
    s = input()
    w="True"
    count=0
    for h in range(0,len(s)):
        st01=(str((s[h].isalpha())))
        st02=(str((s[h].isdigit())))
    if w in st01 or w in st02:
            count=count+1
    if count>0:
        print("True")
    else:
        print("False")
    count1=0
    for i in range(0,len(s)):
        st1=(str((s[i].isalpha())))
        if w in st1:
            count1=count1+1
    if count1>0:
        print("True")
    else:
        print("False")
    count2=0
    for j in range(0,len(s)):
        st2=(str((s[j].isdigit())))
        if w in st2:
            count2=count2+1
    if count2>0:
        print("True")
    else:
        print("False")
    count3=0
    for k in range(0,len(s)):
        st3=(str((s[k].islower())))
        if w in st3:
            count3=count3+1
    if count3>0:
        print("True")
    else:
        print("False")
    count4=0
    for l in range(0,len(s)):
        st4=(str(s[l].isupper()))
        if w in st4:
            count4=count4+1
    if count4>0:
        print("True")
    else:
        print("False")
