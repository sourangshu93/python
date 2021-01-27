list = []
if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        command=input("")
        q=command.split()
        if  q[0]== "insert":
            list.insert(int(q[1]),int(q[2]))
        elif q[0]=="remove":
            list.remove(int(q[1]))
        elif q[0]=="append":
            list.append(int(q[1]))
        elif q[0]=="sort":
            list.sort()
        elif q[0]=="pop":
            list.pop(-1)
        elif q[0]=="reverse":
            list.reverse()
        elif q[0]=="print":
            print(list)