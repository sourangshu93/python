''' The queue ADT stores object.
    The queue works on FIFO mechanism for inserting and delting element.
    Insertion in the rear of the queue.
    Deletion from the front of the queue.
    Operations: Enqueue(object) : Insert at the end of the queue
                Dequeue() : Remove and return at front
                first() : Returns element at front
                len() : Returns no of element
                isempty() : Whether queue is empty or not
    '''
class Queue:
    def __init__(self):
        self.data=[]
    def display(self):
        if len(self.data)==0:
            print("The queue is empty")
        else:
            print("The queue is:",self.data)
    def enqueue(self,e):
        self.data.append(e)
        print("Element",e,"has been enqueued")
    def dequeue(self):
        if len(self.data)==0:
            print("There is no item in the queue to dequeue")
        else:
            n=self.data[0]
            self.data.pop(0)
            print("The element",n,"has been dequeued")
    def first(self):
        if len(self.data)==0:
            print("There is no item in the queue")
        else:
            print("The first element of the queue is:",self.data[0])
    def len(self):
        print("The length of the queue is:",len(self.data))
    def isempty(self):
        if len(self.data)==0:
            print("True")
        else:
            print("False")

q=Queue()
q.display()
q.isempty()
q.len()
q.enqueue(10)
q.enqueue(40)
q.enqueue(60)
q.display()
q.isempty()
q.len()
q.dequeue()
q.display()
q.len()
q.dequeue()
q.display()
q.len()