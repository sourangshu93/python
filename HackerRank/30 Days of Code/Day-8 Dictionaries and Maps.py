# Enter your code here. Read input from STDIN. Print output to STDOUT
def PhoneNumbers(inputs):
    for i in inputs:
        try:
            m=d[i]
            print("{}={}".format(i,m))
        except KeyError:
            print("Not found")

if __name__=="__main__":
    N=int(input())
    d={}
    for n in range(N):
        s=input().split()
        d[s[0]]=s[-1]
    inputs = []
    while True:
        inp = input()
        if inp == "":
            break
        inputs.append(str(inp))
    PhoneNumbers(inputs)