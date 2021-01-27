def is_leap(year):
    leap = False
    non_leap=True
    # Write your logic here
    if (year % 100==0) :
        if (year % 400==0):
            return non_leap
        else:
            return leap
    elif (year % 4==0):
        return non_leap
    else:
        return leap

year = int(input())
print(is_leap(year))