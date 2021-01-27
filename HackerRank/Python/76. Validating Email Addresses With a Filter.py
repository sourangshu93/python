def fun(s):
    a=lambda x,y,z: str(x+"@"+y+"."+z)
    q=s.split("@")
    q1=(q[-1].split("."))
    username=q[0]
    website=q1[0]
    extension=q1[-1]
    if (a(username,website,extension))==s and website.isalnum() and (0<len(extension)<=3) and username.replace("-", "").replace("_", "").isalnum():
        return "True"
def filter_mail(emails):
    return list(filter(fun, emails))
if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)