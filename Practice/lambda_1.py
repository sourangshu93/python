#l=["Marie Curie","Albert Einstein", "Niels Bohr","Issac Newton","Dimitree Mendeleev","Antonie Lavoisier","Carl Linnaeus","Alfred Wegnner","Charles Darwin"]
l1=[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(sorted(l1,key= (lambda x: x[1]),reverse=False))

