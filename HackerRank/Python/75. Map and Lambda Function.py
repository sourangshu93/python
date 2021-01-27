cube = lambda x: x**3# complete the lambda function 
def fibonacci(n):
    a=0
    b=1
    l=[]
    # return a list of fibonacci numbers
    for i in range(n):
        l.append(a)
        a,b=b,a+b
        i=i+1
    return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))