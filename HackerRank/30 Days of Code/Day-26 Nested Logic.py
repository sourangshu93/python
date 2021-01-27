# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
from datetime import date
def NestedLogic(da,ma,ya,de,me,ye):
    dueDate=datetime.datetime(int(ye),int(me),int(de))
    returnDate=datetime.datetime(int(ya),int(ma),int(da))
    m=(returnDate-dueDate)
    w=(m.days)
    if dueDate.year==returnDate.year:
        if w//30==0:
            print(int(m.days)*15)
        if 12>w//30>0:
            p=w//30
            print(p*500)
        if w//30<0  :
            print(0)
    if dueDate.year!=returnDate.year:
        if w//30==0:
            print(10000)
        if w//30>0:
            print(10000)
        if w//30<0  :
            print(0)
if __name__ == '__main__':
    da,ma,ya=input().split()
    de,me,ye=input().split()
    NestedLogic(da,ma,ya,de,me,ye)
