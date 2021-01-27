import numpy as np
class Graph:
    def __init__(self,vertices):
        self.adjMat = np.zeros((vertices,vertices))
        self.vertices = vertices
    def insert_edge(self,u,v,w=1):
        self.adjMat[u][v]=w
    def delete_edge(self,u,v):
        self.adjMat[u][v]=0
    def get_edge(self,u,v):
        return self.adjMat[u][v]
    def vertices_count(self):
        return(self.vertices)
    def edge_count(self):
        count=0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if not self.adjMat[i][j]==0:
                    count=count+1
        return count
    def indegree(self,u):
        count=0
        for i in range(self.vertices):
            if not self.adjMat[i][u]==0:
                count=count+1
        return count
    def outdegree(self,u):
        count=0
        for j in range(self.vertices):
            if not self.adjMat[u][j]==0:
                count=count+1
        return count
    def display(self):
        print(self.adjMat)

G=Graph(7)
print("Graph Adjacency matrix")
G.display()
G.insert_edge(0,1)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(1,6)
G.insert_edge(2,3)
G.insert_edge(2,4)
G.insert_edge(2,6)
G.insert_edge(3,4)
G.insert_edge(4,2)
G.insert_edge(4,5)
G.insert_edge(5,2)
G.insert_edge(5,3)
G.insert_edge(6,3)
print("Graph Adjacency matrix")
G.display()
print("Edge Count:",G.edge_count())
print("Vertices Count:",G.vertices_count())
print("Outdegree:",G.outdegree(3))
print("Indegree:",G.indegree(3))