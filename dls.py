from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DLS(self,src,target,maxDepth):
        
        if src==target:
            return True
        if maxDepth<=0:
            return False
        
        for i in self.graph[src]:
            if(self.DLS(i,target,maxDepth-1)):
                return True
        return False

g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)

source=0;target=6;maxDepth=2;

if g.DLS(source,target,maxDepth)==True:
    print("Reachable")
else:
    print("Not Reachable")