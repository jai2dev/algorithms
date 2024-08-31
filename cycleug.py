from collections import defaultdict

class Graph:
	"""docstring for gra"""
	def __init__(self, ver):
		# super(gra, self).__init__()
		self.ver = ver
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def cycleutil(self,v,visited,parent):
		visited[v]=True

		for i in self.graph[v]:
			if visited[i]==False:
				if self.cycleutil(i,visited,v):
					return True
			elif parent!=i:
				return True

		return False

	def cycle(self):
		visited=[False]*self.ver

		for i in range(self.ver):
			if visited[i]==False:
				if self.cycleutil(i,visited,-1)==True:
					return True

		return False



g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.cycle(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
  
if g1.cycle(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")
