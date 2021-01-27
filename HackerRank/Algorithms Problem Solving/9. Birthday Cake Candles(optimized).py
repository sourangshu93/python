import time
def birthdayCakeCandles(ar):
    start = time.time()
    m=max(ar)
    print(ar.count(m))
    end = time.time()
    print("elapse time:",(end-start))
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
