# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for attr in attrs:
            print("->",attr[0],">",attr[1])
if __name__ == '__main__':
    N=int(input())
    html=""
    for i in range(N):
        html=html+input()
        html+="\n"
    m=MyHTMLParser()
    m.feed(html)