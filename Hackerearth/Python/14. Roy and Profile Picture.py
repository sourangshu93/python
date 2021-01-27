def ProfilePicture(L,W,H):
    if int(W)<L or int(H)<L:
        print("UPLOAD ANOTHER")
    elif (int(W)>=L and int(H)>=L) and int(W)==int(H):
        print("ACCEPTED")
    else:
        print("CROP IT")

if __name__=="__main__":
    L=int(input())
    N=int(input())
    for n in range(N):
        W,H=input().split()
        ProfilePicture(L,W,H)

