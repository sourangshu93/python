import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self, no):
        if (self.imaginary+no.imaginary)>=0:
            q=("%.2f+%.2fi") %((self.real+no.real),(self.imaginary+no.imaginary))
        if (self.imaginary+no.imaginary)<0:
            q="%.2f-%.2fi" %((self.real+no.real),abs(self.imaginary+no.imaginary))
        return q
    def __sub__(self, no):
        if (self.imaginary-no.imaginary)<0:
            r="%.2f-%.2fi" %((self.real-no.real),abs(self.imaginary-no.imaginary))
        if (self.imaginary-no.imaginary)>=0:
             r="%.2f+%.2fi" %((self.real-no.real),(self.imaginary-no.imaginary))
        return r
    def __mul__(self, no):
        #where real and imag both !=0
        if ((self.imaginary*no.real)+(self.real*no.imaginary))>0:
            s="%.2f+%.2fi"%(((self.real*no.real)+((self.imaginary*no.imaginary)*(-1))),abs((self.imaginary*no.real)+(self.real*no.imaginary)))
        if ((self.imaginary*no.real)+(self.real*no.imaginary))<0:
            s="%.2f-%.2fi"%(((self.real*no.real)+((self.imaginary*no.imaginary)*(-1))),abs((self.imaginary*no.real)+(self.real*no.imaginary)))
        if self.imaginary==0 and (self.real*no.imaginary)<0:
            s=("%.2f-%.2fi") %((self.real*no.real),abs(self.real*no.imaginary))
        if self.imaginary==0 and (self.real*no.imaginary)>0:
            s=("%.2f+%.2fi") %((self.real*no.real),abs(self.real*no.imaginary))
        if self.real==0 and (self.imaginary*no.real)<0:
            s=("%.2f-%.2fi") %(((self.imaginary*no.imaginary)*(-1)),abs(self.imaginary*no.real))
        if self.real==0 and (self.imaginary*no.real)>0:
             s=("%.2f+%.2fi") %(((self.imaginary*no.imaginary)*(-1)),abs(self.imaginary*no.real))
        if no.imaginary==0 and (self.imaginary*no.real)<0:
            s=("%.2f-%.2fi") %((self.real*no.real),abs(self.imaginary*no.real))
        if no.imaginary==0 and (self.imaginary*no.real)>0:
            s=("%.2f+%.2fi") %((self.real*no.real),abs(self.imaginary*no.real))
        if no.real==0 and (self.real*no.imaginary)<0:
            s=("%.2f-%.2fi") %(((self.imaginary*no.imaginary)*(-1)),abs(self.real*no.imaginary))
        if no.real==0 and (self.real*no.imaginary)>0:
             s=("%.2f+%.2fi") %(((self.imaginary*no.imaginary)*(-1)),abs(self.real*no.imaginary))
        return s
    def __truediv__(self, no):
        m1=(no.imaginary**2+no.real**2)
        m2=-(no.imaginary**2)
        if no.imaginary>0 :
            if (((self.imaginary*no.real)-(self.real*no.imaginary))/m1)<0:
                t="%.2f-%.2fi" %((((self.real*no.real)-((self.imaginary*no.imaginary)*(-1)))/m1),abs(((self.imaginary*no.real)-(self.real*no.imaginary))/m1))
            if (((self.imaginary*no.real)-(self.real*no.imaginary))/m1)>0:
                t="%.2f%+.2fi" %((((self.real*no.real)-((self.imaginary*no.imaginary)*(-1)))/m1),abs(((self.imaginary*no.real)-(self.real*no.imaginary))/m1))
            if no.real==0 and ((self.real*no.imaginary)/m2)>0:
                t=("%.2f+%.2fi") %((((self.imaginary*no.imaginary)*(-1))/m2),abs((self.real*no.imaginary)/m2))
            if no.real==0 and ((self.real*no.imaginary)/m2)<0:
                t=("%.2f-%.2fi") %((((self.imaginary*no.imaginary)*(-1))/m2),abs((self.real*no.imaginary)/m2))
            if self.real==0 and ((self.imaginary*no.real)/m1)>0:
                t=("%.2f+%.2f") %((((self.imaginary*(-no.imaginary))*(-1))/m1),abs((self.imaginary*no.real)/m1))
            if self.real==0 and ((self.imaginary*no.real)/m1)<0:
                t=("%.2f-%.2f") %((((self.imaginary*(-no.imaginary))*(-1))/m1),abs((self.imaginary*no.real)/m1))
        if no.imaginary<0 :
            if (self.real*(-no.imaginary)+(self.imaginary*no.real))>0:
                t="%.2f+%.2fi" %((((self.real*no.real)+((-no.imaginary)*self.imaginary)*(-1))/m1),abs((self.real*(-no.imaginary)+(self.imaginary*no.real))/m1))
            if (self.real*(-no.imaginary)+(self.imaginary*no.real))<0:
                t="%.2f-%.2fi" %((((self.real*no.real)+((-no.imaginary)*self.imaginary)*(-1))/m1),abs((self.real*(-no.imaginary)+(self.imaginary*no.real))/m1))
            if (((self.imaginary*no.real)+(self.real*no.imaginary))/m1)<0:
                t="%.2f-%.2fi" %((((self.real*no.real)+((self.imaginary*no.imaginary)*(-1)))/m1),abs(((self.imaginary*no.real)+(self.real*no.imaginary))/m1))
            if (((self.imaginary*no.real)-(self.real*no.imaginary))/m1)>0:
                t="%.2f+%.2fi" %((((self.real*no.real)-((self.imaginary*no.imaginary)*(-1)))/m1),abs(((self.imaginary*no.real)-(self.real*no.imaginary))/m1))
            if no.real==0 and ((self.real*no.imaginary)/m2)>0:
                t=("%.2f+%.2fi") %((((self.imaginary*no.imaginary)*(-1))/m2),abs((self.real*no.imaginary)/m2))
            if no.real==0 and ((self.real*no.imaginary)/m2)<0:
                t=("%.2f-%.2fi") %((((self.imaginary*no.imaginary)*(-1))/m2),abs((self.real*no.imaginary)/m2))
            if self.real==0 and ((self.imaginary*no.real)/m1)>0:
                t=("%.2f+%.2fi") %((((self.imaginary*(-no.imaginary))*(-1))/m1),abs((self.imaginary*no.real)/m1))
            if self.real==0 and ((self.imaginary*no.real)/m1)<0:
                t=("%.2f-%.2fi") %((((self.imaginary*(-no.imaginary))*(-1))/m1),abs((self.imaginary*no.real)/m1))
            if self.imaginary==0 and ((self.real*(-no.imaginary))/m1)>0:
                t=("%.2f+%.2fi") %(((self.real*no.real)/m1),abs((self.real*(-no.imaginary))/m1))
            if self.imaginary==0 and ((self.real*(-no.imaginary))/m1)<0:
                t=("%.2f-%.2fi") %(((self.real*no.real)/m1),abs((self.real*(-no.imaginary))/m1))
        if no.imaginary==0:
            if self.imaginary<0 and (self.imaginary/no.real)<0:
                t=("%.2f-%.2fi") %((self.real/no.real),abs(self.imaginary/no.real))
            if self.imaginary<0 and (self.imaginary/no.real)>0:
                t=("%.2f+%.2fi") %((self.real/no.real),abs(self.imaginary/no.real))
            if self.imaginary>0 and (self.imaginary/no.real)<0:
                t=("%.2f-%.2fi") %((self.real/no.real),abs(self.imaginary/no.real))
            if self.imaginary>0 and (self.imaginary/no.real)>0:
                t=("%.2f+%.2fi") %((self.real/no.real),abs(self.imaginary/no.real))
        if (no.real==(-self.real)) and no.imaginary==(-self.imaginary):
            t=("%.2f+%.2fi")%(-1,0)
        if no.real==(-no.imaginary) and self.real==(-self.imaginary):
            t=("%.2f+%.2fi")%((self.real/no.real),0)
        if (no.real==self.real) and (no.imaginary==self.imaginary):
            t=("%.2f+%.2fi")%((1,0))
        return t
    def mod(self):
        m="%.2f+0.00i" %(math.sqrt(self.real**2+self.imaginary**2))
        return m
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')