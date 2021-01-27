def split_and_join(line):
    n=line.split(" ")
    for word in n:
        a=("-").join(n)
    return(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)