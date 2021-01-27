def BookIsbn(N):
    sum=0
    for i in range(1,len(N)+1):
        sum+=i*int(N[i-1])
    print ("Legal ISBN") if sum%11==0 else print ("Illegal ISBN")

if __name__ == "__main__":
    N=input()
    BookIsbn(N)