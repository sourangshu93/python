import string
n=string.digits
p=(((len(n)*len(n))-len(n))//len(n))
q=(p*p-len(n)-(len(n)//len(n)))
for i in range(q,p*p):
    print(i)
