from dateutil import parser
for _ in range(int(input())):
    d1 = parser.parse(input().strip())
    d2 = parser.parse(input().strip())
    print(abs(int((d2-d1).total_seconds())))