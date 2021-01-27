class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    
    def is_empty(self):
        print(bool(self.size==0))

    def add_first(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.size+=1

    def add_last(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.size+=1

    def add_any(self,data,pos):
        newnode=Node(data)
        thead=self.head
        i=1
        while i < pos:
            thead=thead.next
            i+=1
        newnode.next=thead.next
        thead.next=newnode
        self.size+=1

    def delete_first(self):
        if not self.head:
            print("Empty linked list")
        else:
            self.head=self.head.next
        self.size-=1
    
    def delete_last(self):
        thead=self.head
        i=0
        if not self.head:
            print("Empty linked list")
        while i< len(self)-2:
            thead=thead.next
            i=i+1
        thead.next=None
        self.size-=1
    
    def delete_any(self,pos):
        thead=self.head
        i=0
        if not self.head:
            print("Empty linked list")
        while i < pos-1:
            thead=thead.next
            i+=1
        thead.next=thead.next.next
        self.size-=1


    def display(self):
        thead=self.head
        if thead is None:
            print('The linked list is empty')
        while thead:
            print(thead.data, end="-->")
            thead=thead.next
        print()

l=LinkedList()
l.is_empty()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_first(5)
l.add_any(15,2)
l.add_first(0)
l.add_last(40)
l.display()
l.delete_first()
l.display()
l.delete_last()
l.display()
l.delete_any(3)
l.display()