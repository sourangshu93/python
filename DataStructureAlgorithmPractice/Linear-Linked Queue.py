class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedQueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
# Queue enqueue operation
    def enqueue(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            self.tail=new
            self.size+=1
        else:
            self.tail.next=new
            self.tail=new
            self.size+=1
# Dequeue Operation
    def dequeue(self):
        if self.head==None:
            print("The queue is empty")
        else:
            self.head=self.head.next
            self.size-=1
# Display method
    def display(self):
        thead=self.head
        if thead==None:
            print("The queue is empty")
        while thead:
            print(thead.data,end="-->")
            thead=thead.next
        print()

l=LinkedQueue()
l.display()
l.enqueue(10)
l.enqueue(20)
l.enqueue(30)
l.enqueue(40)
l.enqueue(50)
l.display()
l.dequeue()
l.dequeue()
l.display()