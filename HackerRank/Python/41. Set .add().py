# Enter your code here. Read input from STDIN. Print output to STDOUT

def DistinctStamps(countries):
    print(len(countries))
if __name__ == '__main__':
    N=int(input())
    countries=set()
    for c in range(N):
        countries.add(str(input()))
    DistinctStamps(countries)