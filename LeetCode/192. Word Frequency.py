'''Write a bash script to calculate the frequency of each word in a text file words.txt.
For simplicity sake, you may assume:
words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
Example:
Assume that words.txt has the following content:
the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
'''
file=open("C:\\Users\\kundus6\\Desktop\\words.txt","r")
lines=file.readlines()
d={}
nl=[]
for line in lines:
    line.replace("\n","")
    l=list(map(str,line.split()))
    nl=nl+l
for s in nl:
    d[s]=nl.count(s)
print(d)
for i in sorted(d.items(),key=lambda x: x[1],reverse=True):print(i[0],i[1])
