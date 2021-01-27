if __name__=="__main__":
    length,pages=input().rstrip().split()
    print("Take Medicine") if int(length)<=23 and 500<=int(pages)<=1000 else print("Don't take Medicine")