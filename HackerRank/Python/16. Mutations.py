def mutate_string(string, position, character):
    l=list(s)
    for f,e in enumerate(l):
        if f==int(i):
            l[f]= c
    q="".join(l)
    return(q)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
