import string
user="dbcjdvchjsdbjhk"
q=[]
for i in user:
    if i not in (string.ascii_letters+string.digits+"_-"):
        print("False")
        break
    else:
        print("True")
