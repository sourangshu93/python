#HackerEarth Challange:Number of cycles
def NoOfCycles(Q,N):
    n=((N**2)-(N-1))
    print(n)

if __name__ == '__main__':
    Q=int(input())
    for q in range(Q):
        N=int(input())
        NoOfCycles(Q,N)