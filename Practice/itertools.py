import itertools

stuff = ['A', 'B', 'C', 'D', 'C', 'D', 'C']
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        print(subset)
