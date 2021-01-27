from googlesearch import search
import datetime
start=datetime.datetime.now()
txt="python"
for i in search(txt,tld='com',num=10,stop=10,pause=2):
    print(i)
end=datetime.datetime.now()
print("Total elapse time:",(end-start))