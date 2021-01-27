'''
# Input Format
A single line containing the space separated values of  and .
#Constraints
5 < N <101
15 < M <303
#Output Format
Output the design pattern.
'''
height, width = map(int,input().split())
# This is above part
for i in range (1,height,2):
    print(((".|.")*i).center(width,"-"))
# This is center
print("WELCOME".center(width,"-"))
# This is Bottom Part
for j in range ((height-2),0,-2):
    print((((".|.")*j).center(width,"-")))