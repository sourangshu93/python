import operator
from operator import itemgetter
l=["Marie Curie","Albert Einstein", "Niels Bohr","Issac Newton","Dimitree Mendeleev","Antonie Lavoisier","Carl Linnaeus","Alfred Wegnner","Charles Darwin"]
l1=[]
for i in l:
    l1.append(i.split())
q=(sorted(l1,key=itemgetter(-1),reverse=False))
l2=[]
for j in q:
    l2.append(' '.join(j))

print(l2)
