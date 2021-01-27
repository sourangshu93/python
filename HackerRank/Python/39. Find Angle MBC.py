# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def FindAngle(a,b):
    c=math.atan(a/b)
    c1=round((math.degrees(c)))
    print((c1),end="") #Since the triangle is a isosceles triangle so angle c will be equal to angle theta.
    degree_sign= u'\N{DEGREE SIGN}'
    print(degree_sign)
if __name__ == '__main__':
    a=int(input())
    b=int(input())
    FindAngle(a,b)