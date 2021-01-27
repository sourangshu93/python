def solve (A):
    # Write your code here
    fh=A[:(N//2)]
    sh=A[(N//2):]
    s=""
    for i in fh:
        s=s+(str(i)[0])
    for j in sh:
        s=s+(str(j)[-1])
    if int(s)%11==0:
        return "OUI"
    else: 
        return "NON"
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    out_ = solve(A)
    print(out_)