n=int(input())
m=int(input())
def floodfill(i,j):
    if i>=n or j>=m or mat[i][j]==-1 or mat[i][j]==0 or i<0 or j<0:
        return 0
    else:
        mat[i][j]=-1
        return 1+(floodfill(i+1,j)+floodfill(i-1,j)+floodfill(i,j+1)+floodfill(i,j-1)+floodfill(i+1,j-1)+floodfill(i+1,j+1)+floodfill(i-1,j-1)+floodfill(i-1,j+1))

mat=[]
res=-999
for i in range(n):
    mat.append([int(x) for x in input().split()]) 

for i in range(n):
    for j in range(m):
        res=max(res,floodfill(i,j))
print(res)        