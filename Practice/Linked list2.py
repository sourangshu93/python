class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def displayList(self):
        a=self.head
        if a is None:
            print("The list is empty!!")
        while a:
            print(a.data,end=" ")
            a=a.next
        print("\n")
    def countNodes(self):
        new=self.head
        n=0
        while new is not None:
            n=n+1
            new=new.next
        print("The no of nodes are:",n)
    def search(self,data):
        a=self.head
        p=1
        while a is not None:
            if a.data==data:
                print(data,"is in position :",p)
                return True
            p=p+1
            a=a.next
        else:
            print(data,"is not present in the list")
            return False
    def insertBegining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def insertEnd(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            return
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=new
    def insertAfterPosition(self,data,position):
        pass
    def insertBeforePosition(self,data,position):
        pass
    def insertAtPosition(self,data,position):
        pass
    def create_list(self):
        N=int(input("Enter the no of Nodes :"))
        if N==0:
            return
        for n in range(N):
            data=int(input("Enter the element to be inserted :"))
            self.insertBegining(data)
            n=n+1

list=LinkedList()
list.create_list()

while True:
    print("1: Display List")
    print("2: Count the Number of Nodes")
    print("3: Search for an Element(Not Implemented)")
    print("4: Insert in an empty List or in the begining of a List")
    print("5: Insert a Node at the end of the list")
    print("6: Insert a Node after a specified node")
    print("7: Insert a Node before a specified node")
    print("8: Insert a Node in the given position")
    print("9: Delete first node")
    print("10: Delete last node")
    print("11: Delete any node")
    print("12: Reverse the list")
    print("13: Bubble sort by exchanging data")
    print("14: Bubble sort by exchanging links")
    print("15: Merge sort")
    print("16: Insert cycle")
    print("17: Detect cycle")
    print("18: Remove cycle")
    print("19: Quit")

    option=int(input("Enter a cholice Between 1-19 :"))
    if option==1:
        list.displayList()
    elif option==2:
        list.countNodes()
    elif option==3:
        data = int(input("Insert an element to be serached :"))
        list.search(data)
    elif option==4:
        data=int(input("Enter an element to be inserted at begining :"))
        list.insertBegining(data)
    elif option==5:
        data=int(input("Enter an element to be entered at the end :"))
        list.insertEnd(data)
    elif option==6:
        data=int(input("Enter an element to be inserted :"))
        position=int(input("Enter the position after what the data has to be inserted :"))
        list.insertAfterPosition(data,position)
    elif option==7:
        data=int(input("Enter an element to be inserted :"))
        position=int(input("Enter the position before what the data has to be inserted:"))
        list.insertBeforePosition(data,position)
    elif option==8:
        data=int(input("Enter an element to be inserted :"))
        position=int(input("Enter the position where the data has to be inserted:"))
        insertAtPosition(data,position)
    elif option==9:
        list.deleteFirstNode()
    elif option==10:
        list.deleteLastNode()
    elif option==11:
        data=int(input("Enter a data to be deleted :"))
        list.deleteNode(data)
    elif option==12:
        list.reverseList()
    elif option==13:
        list.bubbleSortData()
    elif option==14:
        list.bubbleSortLinks()
    elif option==15:
        list.mergesortList()
    elif option==16:
        list.insertCycle()
    elif option==17:
        list.detectCycle()
    elif option==18:
        list.removeCycle()
    elif option==19:
        exit()
