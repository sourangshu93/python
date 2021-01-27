'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def ResaonsWhy(a,b,c):
    tmp=a
    a=b
    b=tmp
    print(int(a)*int(c),int(b)+int(c))
    
if __name__ == '__main__':
    a,b,c=input().split()
    ResaonsWhy(a,b,c)