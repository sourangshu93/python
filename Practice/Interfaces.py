class AdvancedArithmetic:
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        pass
    def divisorSum(self, n):
        div=[]
        for i in range (0,n+1):
            if (n%i==0):
                div.append(i)
        print(div)
        return sum(div)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)