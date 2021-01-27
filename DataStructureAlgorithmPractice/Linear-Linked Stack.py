class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedStack:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def push(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail=new
        self.size=self.size+1
    def pop(self):
        if self.head==None:
            print("Empty stack")
        thead=self.head
        i=0
        while i < len(self)-2:
            thead=thead.next
            i=i+1
            val=thead.next.data
        thead.next=None
        self.tail=thead
        print(val,"Has been popped")
    def top(self):
        if self.head==None:
            print("Empty stack")
        else:
            print("Last Element:",self.tail.data)
    def display(self):
        thead=self.head
        if thead==None:
            print("Empty stack")
        while thead:
            print(thead.data,end="-->")
            thead=thead.next
        print()

L=LinkedStack()
L.push(10)
L.push(20)
L.push(30)
L.push(40)
L.push(50)
L.push(60)
L.top()
L.display()
L.pop()
L.display()
L.top()