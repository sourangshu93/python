if __name__=="__main__":
    T=int(input())
    for t in range(T):
        s=input()
        if "00" in s:
            s.replace("00","")
        if "11" in s:
            s.replace("11","")
    print(s)
