import datetime
from datetime import datetime
from datetime import time
from datetime import timedelta
def Duration(SH,SM,EH,EM):
    start = timedelta(hours = int(SH),minutes= int(SM))
    end = timedelta(hours = int(EH),minutes = int(EM))
    t=str(end-start).split(":")
    print(int(t[0]), int(t[1]))
if __name__ == "__main__":
    N=int(input())
    for n in range(N):
        SH,SM,EH,EM=input().rstrip().split()
        Duration(SH,SM,EH,EM)


