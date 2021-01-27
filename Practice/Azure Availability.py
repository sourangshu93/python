def AzureAvailability(t):
    dif=(100-t)
    downtime=(dif*365*24*3600)
    if downtime <60:
        print("Yearly Downtime",round(downtime),"seconds")
    if 60 < downtime<3600:
        print("Yearly Downtime",round(downtime//60),"minutes",round(downtime%60),"seconds")
    if downtime >3600:
        print("Yearly Downtime",round(downtime//3600),"hours",round((downtime%3600)//60),"minutes",round((downtime%3600)%60),"seconds")

if __name__=="__main__":
    t=float(input())
    AzureAvailability(t)