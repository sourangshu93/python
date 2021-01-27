def Maze(S):
    LR=0
    UD=0
    for s in S:
        if s=="L":
            LR=LR-1
        if s=="R":
            LR=LR+1
        if s=="U":
            UD=UD+1
        if s=="D":
            UD=UD-1
    print(LR,UD)
if __name__=="__main__":
    S=input()
    Maze(S)