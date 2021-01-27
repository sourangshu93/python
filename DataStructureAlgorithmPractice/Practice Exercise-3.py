class Fraction:
    def __init__(self,nr,dr=1):
        self.nr=nr
        self.dr=dr
        if dr < 0 :
            self.nr *=-1
            self.dr *=-1

    def show(self):
        print("{}{}{}".format(self.nr,"/",self.dr))

    def multiply(self,frac):
        fun=Fraction(frac)
        a=self.nr*fun.nr
        b=self.dr*fun.dr
        print("{}{}{}".format(a,"/",b))

f=Fraction(10,20)
f.show()
f.multiply(10)