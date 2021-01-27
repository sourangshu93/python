import re
def Transcription(N):
    if not (re.fullmatch("[ATGC]+",N)):
        print("Invalid Input")
    else:
        for n in N:
            if n=="G":
                print("C",end="")
            if n=="C":
                print("G",end="")
            if n=="T":
                print("A",end="")
            if n=="A":
                print("U",end="")

if __name__ == '__main__':
    N=str(input())
    Transcription(N)    