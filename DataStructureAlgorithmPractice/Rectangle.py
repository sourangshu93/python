class Rectange:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    @property
    def diagonal(self):
        return("Diagonal:",(self.length*self.length+self.width*self.width)**0.5)

    def area(self):
        print("Area:",self.width*self.length)
        
    def perimeter(self):
        print("Perimeter:",2*(self.width+self.length))

r=Rectange(20,10)
print(r.diagonal)
r.area()
r.perimeter()
r.length=30
print(r.diagonal)
r.area()
r.perimeter()