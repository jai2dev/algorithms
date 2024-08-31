from collections import defaultdict,deque
# import deque

class Kahns:
	def __init__(self,nodes,n):
		self.nodes=nodes
		self.totalNodes=n


	def topologicalSort(self):
		graph=defaultdict(lambda:[])
		indegree=[0]*self.totalNodes
		for u,v in self.nodes:
			graph[u].append(v)
			indegree[v]+=1

		queue=deque()
		for i in range(self.totalNodes):
			if indegree[i]>0:continue
			queue.append(i)

		ans=[]
		while queue:
			u=queue.popleft()
			ans.append(u)
			for v in graph[u]:
				indegree[v]-=1
				if indegree[v]==0:
					queue.append(v)
		return ans


if __name__ == '__main__':
	graphObj=Kahns([[0,1],[2,3],[1,2],[0,3]],4)
	print(graphObj.topologicalSort())







