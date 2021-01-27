if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr1=list(set(arr))
    arr1.sort()
    print(arr1[-2])