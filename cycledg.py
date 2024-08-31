from collections import defaultdict

class Graph:
	"""docstring for Graph"""
	def __init__(self, ver):
		# super(Graph, self).__init__()
		self.ver = ver
		self.graph=defaultdict(list)


	def addEdge(self,u,v):
		self.graph[u].append(v)

	def cycleutil(self,v,visited,rec):
		
		visited[v]=True
		rec[v]=True

		for i in self.graph[v]:
			if visited[i]==False:
				if self.cycleutil(i,visited,rec):
					return True

			elif rec[i]==True:
				return True

		rec[v]=False

		return False

	def cycle(self):
		
		visited=[False]*self.ver

		rec=[False]*self.ver

		for i in range(self.ver):

			if visited[i]==False:
				if self.cycleutil(i,visited,rec)==True:
				    return True

		return False




g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.cycle(): 
    print ("Graph has a cycle")
else: 
    print( "Graph has no cycle")


