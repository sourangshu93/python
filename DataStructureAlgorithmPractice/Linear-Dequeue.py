class Dequeue:
    def __init__(self):
        self.data=[]

    def is_empty(self):
        return len(self.data)==0

    def display(self):
        if len(self.data)==0:
            print("The dequeue is empty")
        else:
            print(self.data)

    def first(self):
        if self.is_empty():
            print("The dequeue is empty")
        else:
            print("The first element is:",self.data[0])
    def insert_front(self,val):
        self.data.insert(0,val)
        print(val,"Has ben inserted in the front of the dequeue")

    def insert_back(self,val):
        self.data.append(val)
        print(val,"Has been inserted in the back of the dequeue")

    def delete_front(self):
        a=self.data[0]
        self.data.pop(0)
        print(a,"has been deleted from the front of the queue")

    def delete_back(self):
        b=self.data[-1]
        self.data.pop()
        print(b,"has been deleted from the back of the queue")
    
f=Dequeue()
f.first()
f.insert_front(10)
f.first()
f.insert_front(20)
f.insert_front(30)
f.first()
f.display()
f.insert_back(5)
f.insert_back(1)
f.display()