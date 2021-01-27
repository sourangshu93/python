import itertools
from itertools import permutations
from itertools import combinations
def vowels(s):
    print(list(permutations(s,2)))



if __name__=="__main__":
    T=int(input())
    for t in range(T):
        s=input()
        vowels(s)