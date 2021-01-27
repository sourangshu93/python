def wrapper(f):
    def fun(l):
        m=[]
        for i in l:
           s=" ".join(["+91",i[-10:-5],i[-5:]])
           m.append(s)
        return f(m)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

