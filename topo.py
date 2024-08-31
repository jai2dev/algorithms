from collections import defaultdict

class Graph:
	"""docstring for Graph"""
	def __init__(self,ver):
		# super(Graph, self).__init__()
		self.graph = defaultdict(list)
		self.ver=ver

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def topoutil(self,v,visited,stack):
		
		visited[v]=True

		for i in self.graph[v]:
			if visited[i]==False:
				self.topoutil(i,visited,stack)

		stack.insert(0,v)


	def toppo(self):
		visited=[False]*self.ver
		stack=[]

		for i in range(self.ver):
			if visited[i]==False:
			    self.topoutil(i,visited,stack)

		return stack


if __name__ == '__main__':
	g=Graph(6)

	g.addEdge(5,2)
	g.addEdge(5,0)
	g.addEdge(4,0)
	g.addEdge(4,1)
	g.addEdge(2,3)
	g.addEdge(3,1)

	print(g.toppo())
		

