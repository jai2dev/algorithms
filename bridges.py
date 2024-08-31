from collections import defaultdict as dt
import sys
sys.setrecursionlimit(10**9)


class Graph:
	def __init__(self,nodes):
		self.graph=dt(lambda:[])
		self.nodes=nodes
		self.bridges=[]


	def add_edge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def dfs(self,u,lowest_reachable_node,time_of_insertion,visited,time,par):
		time_of_insertion=lowest_reachable_node=time+1
		visited[u]=1

		for v in self.graph[u]:
			if not visited[v]:
				self.dfs(v,lowest_reachable_node,time_of_insertion,visited,time+1,u)
				lowest_reachable_node[u]=min(lowest_reachable_node[u],lowest_reachable_node[v])

				if lowest_reachable_node[v]>time_of_insertion[u]:
					self.bridges.append((u,v))

			elif visited[v] and v!=par:
				lowest_reachable_node[u]=min(lowest_reachable_node[u],lowest_reachable_node[v])

		



if __name__ == '__main__':
	graph=Graph(15)

	for i,j in zip(range(10),range(15,5,-1)):
		g.add_edge(i,j)

	g.dfs(0,[0]*15,[0]*15,[0]*15,0,-1)

