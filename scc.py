from collections import defaultdict

class Graph:
	"""docstring for Graph"""
	def __init__(self, ver):
		# super(Graph, self).__init__()
		self.ver = ver
		self.graph= defaultdict(list)


	def addEdge(self,u,v):
		self.graph[u].append(v)

	def dfsutil(self,v,visited,scc):
		visited[v]=True

		scc.append(v)

		for i in self.graph[v]:
			if visited[i]==False:
				scc=self.dfsutil(i,visited,scc)
		return scc
		# stack.append(v)


	def rev_order(self,v,visited,stack):
		# visited=[False]*self.ver
		visited[v]=True
		
		# stack=[]
		# stack.append(v)

		for i in self.graph[v]:
			if visited[i]==False:
				self.rev_order(i,visited,stack)

		stack.append(v)
		

	def transpose(self):
		g=Graph(self.ver)

		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)

		return g

	def kosaraju(self):
		# r=rev_order()
		# reverse=reversed(r)

		visited=[False]*self.ver

		stack=[]

		# strong_comps=[]

		for i in range(self.ver):
			if visited[i]==False:
				self.rev_order(i,visited,stack)





		gr=self.transpose()

		visited=[False]*self.ver
		scc=[]

		for i in stack[::-1]:
			if visited[i]==False:
				scomps=[]
				scc.append(gr.dfsutil(i,visited,scomps))

		return scc



g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
   
print ("Following are strongly connected components " +
                           "in given graph") 
print(g.kosaraju() )
			
		