class Difference:
    def __init__(self, a):
        self.__elements = a
    
	# Add your code here
    def computeDifference(self):
        l=[]
        for i in range(1,len(a)):
            l.append(abs(a[0]-a[i]))
        Difference.maximumDifference=max(l)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
