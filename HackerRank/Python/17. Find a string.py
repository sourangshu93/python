def count_substring(string, sub_string):
    l=list(string)
    p=len(sub_string)
    count=0
    for i in range(0, len(l)):
        nl=l[(0+i):(p+i)]
        i=i+1
        if len(nl)==p:
            q="".join(nl)
            if sub_string in q:
                count=count+1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
