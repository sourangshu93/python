''' Implementaton of stack works on LIFO mechanism for insert and delete operation.
    Stack ADT stores object.
    Operations: push(object) : Pust element into the stack
                pop() : Delete element from stack
                top() : Displays last inserted element in queue
    '''

class Stack:
    def __init__(self):
        self.data=[]
    def display(self):
        if len(self.data)==0:
            print("The stcak is empty")
        else:
            print("The stack is:",self.data)
    def push(self,e):
        self.data.append(e)
        print("Element",e,"has been pushed to the stack")
    def pop(self):
        if len(self.data)==0:
            print("Empty stack,cannot pop item")
        else:
            self.data.pop()
            print(self.data[-1],"Has been popped out from the stack")
    def top(self):
        if len(self.data)==0:
            print("The stack does not have any item")
        else:
            print(self.data[-1],"Is the last inserted element in the stack")
st=Stack()
st.display()
st.pop()
st.top()
st.push(10)
st.push(20)
st.push(30)
st.top()
st.display()