from collections import defaultdict

class Graph:
	"""docstring for Graph"""
	def __init__(self, ver):
		# super(Graph, self).__init__()
		self.ver = ver
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def util(self,v,visited,compo):
		visited[v]=True

		compo.append(v)

		for i in self.graph[v]:
			if visited[i]==False:
				compo=self.util(i,visited,compo)
		return compo

	def conncompo(self):
		visited=[False]*self.ver

		cc=[]

		for i in range(self.ver):
			if visited[i]==False:
				compo=[]
				cc.append(self.util(i,visited,compo))
		return cc

if __name__=="__main__": 
      
    # Create a graph given in the above diagram 
    # 5 vertices numbered from 0 to 4 
    g = Graph(5); 
    g.addEdge(1, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 4) 
    cc = g.conncompo() 
    print("Following are connected components") 
    print(cc) 



