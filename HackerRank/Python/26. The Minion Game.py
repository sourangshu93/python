import re
def minion_game(string):
    # your code goes here
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]
    l1=[]
    l2=[]
    for k in res:
        if re.search('^[A,E,I,O,U]',k):
            l1.append(k)
        if re.search('^[^A,E,I,O,U]',k):
            l2.append(k)
    if len(l1) > len(l2):
        print("Kevin",len(l1))
    elif len(l2)>len(l1):
        print("Stuart",len(l2))
    elif len(l2)==len(l1):
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)