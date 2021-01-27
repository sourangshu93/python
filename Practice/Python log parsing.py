file=open("C:\\Users\\kundus6\\Desktop\\log.txt",'r')
lines=file.readlines()
l1=[]
l2=[]
for i in range(len(lines)):
    if lines[i]=="STATE=SUCCESS\n":
        l1.append(int(lines[i+1].replace("TIME=","").replace("S","").replace("\n","")))
    if lines[i]=="STATE=FAILED\n":
        l2.append(int(lines[i+1].replace("TIME=","").replace("S","").replace("\n","")))

print(("No of successful event(s) is/are {},and average elapse time for successful event(s) is/are {} seconds").format(len(l1),sum(l1)/len(l1)))
print(("No of failed event(s) is/are {}, and average elapse time for failed event(s) is/are {}").format(len(l2),sum(l2)/len(l2)))
