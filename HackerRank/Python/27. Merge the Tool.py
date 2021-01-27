import itertools
def merge_the_tools(string, k):
    t=int((len(string))//k)
    li=[]
    for i in range(0,len(string),k):
        j=string[i:i+k]
        li.append(j)
    print(li)
    for k in li:
        q=(list(k))
        nli=[]
        for l in q:
            if l not in nli:
                nli.append(l)
        print("".join(nli))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)