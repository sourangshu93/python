# Enter your code here. Read input from STDIN. Print output to STDOUT
def average(array):
    new_array=list(set(array))
    l=len(new_array)
    s=sum(new_array)
    average=s/l
    print(average)
if __name__ == '__main__':
    N=int(input())
    array=list(map(int,input().split()))
    average(array)