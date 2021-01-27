class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root==None:
            return 0
        else:
            lheight=self.getHeight(root.left)
            rheight=self.getHeight(root.right)
            if lheight==None:
                return (rheight+1)
            if rheight==None:
                return (lheight+1)
            if lheight!=None and lheight!=None and (lheight < rheight):
                return (rheight+1)
            if lheight!=None and lheight!=None and (lheight > rheight):
                return (lheight+1)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       