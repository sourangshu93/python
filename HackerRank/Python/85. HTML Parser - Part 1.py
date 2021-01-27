# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("Start :",tag)
        for attr in attrs:
            print("->",attr[0],">",attr[1])
    def handle_endtag(self,tags):
        print("End   :",tags)
    def handle_startendtag(self, tag1, attr0):
        print("Empty :",tag1)
        for att1 in attr0:
           print("->",att1[0],">",att1[1])
if __name__ == '__main__':
    N=int(input())
    s=""
    for n in range(N):
        s=s+str(input())
    parser = MyHTMLParser()
    parser.feed(s)
        