from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
def AgeCalculator(n):
    today=datetime.today()
    dob=datetime(n[-1],n[1],n[0])
    diff=today-dob
    year=(int(diff.days)//365)
    month=((int(diff.days)%365)//30)
    days=((int(diff.days)%365)%30)
    print(year)
    print(month)
    print(days)
    
if __name__ == "__main__":
    n=list(map(int,input('Input date in format dd<space>mm<space>yyyy: ').rstrip().split()))
    AgeCalculator(n)

