from collections import defaultdict

class Graph:
	"""docstring for Graph"""
	def __init__(self):
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def dfs(self,v,visited):
		visited[v]=True
		print(v,end=' ')
		
		for i in self.graph[v]:
			if visited[i]==False:
				self.util(i,visited)

	def DFS(self,v):
		visited=[False]*(max(self.graph)+1)

		self.dfs(v,visited)

if __name__ == '__main__':
	g=Graph()
	# edges=[(0,1),(0,2),(1,2),(2,0)]
	# graph=defaultdict(lambda:[])
	# for u,v in edges:
	# 	graph[u].append(v)
	# 	graph[v].append(u)

	# for v in graph[u]:


	g.addEdge(0,1)
	g.addEdge(0,2)
	g.addEdge(1,2)
	g.addEdge(2,0)
	g.addEdge(2,3)
	g.addEdge(3,3)

	g.DFS(2)
