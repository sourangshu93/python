def Permutation(n,s):
    if n==1:
        return s
    return[i+j for i in Permutation(1,s) for j in Permutation(n-1,s)]

print(Permutation(3,"ABC"))
