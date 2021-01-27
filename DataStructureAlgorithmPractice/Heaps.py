class Heaps:
    def __init__(self):
        self.maxsize=10
        self.data=[-1]*self.maxsize
        self.currentsize=0
    def maxh(self):
        if self.currentsize==0:
            print("The heap is empty")
        else:
            return self.data[1]
    def insert(self):
        if self.currentsize==self.maxsize:
            print("No space in heap")
    