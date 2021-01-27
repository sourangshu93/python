li1=['a','b']
li2=['a','b','a','a','b']
indices = [i for i, x in enumerate(li2) if x == "a"]
print (indices)

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for j in d.items():
    print(" ".join((list(j)[-1])))
    
1 2
abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxx
abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxx
abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxxy
