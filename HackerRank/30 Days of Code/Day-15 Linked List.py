class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        self.head=head
        node = Node(data)
        node.next=self.head
        self.head=node
        return node
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 