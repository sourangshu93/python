def print_formatted(number):
    q=len(bin(number)[2::])
    # Convert to Octal
    for i in range (1,number+1):
        print(((str(i).rjust(q," "))+((str(oct(i)[2::])).rjust(q+1," "))+((str((hex(i)).upper()[2::])).rjust(q+1," "))+(str(bin(i)[2::].rjust(q+1," ")))))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)