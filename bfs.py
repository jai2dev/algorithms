from collections import defaultdict
class Graph:
	"""docstring for Graph"""
	def __init__(self):
		# super(Graph, self).__init__()
		# self.arg = arg
		self.graph= defaultdict(list)


	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self,s):
		queue=[]
		visited=[False]*(len(self.graph))
		queue.append(s)
		visited[s]=True
		bfs=[]
		while queue:
			v=queue.pop(0)
			bfs.append(v)
			for i in self.graph[v]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True

		return bfs


	def bfsTree(self,root):
		queue=deque()
		queue.append(root)
		ans=[]
		while queue:
			curSize=len(queue)
			temp=[]
			for _ in range(curSize):
				curRoot=queue.popleft()
				temp.append(curRoot.val)
				if curRoot.left:
					queue.append(curRoot.left)
				if curRoot.right:
					queue.append(curRoot.right)
			ans.append(temp)
		return ans





if __name__ == '__main__':
	g=Graph()

	g.addEdge(0,1)
	g.addEdge(0,2)
	g.addEdge(1,2)
	g.addEdge(2,0)
	g.addEdge(2,3)
	g.addEdge(3,3)

	print(g.BFS(2))


