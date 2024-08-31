from collections import defaultdict as dt

from heapq import heappush, heappop
from math import log2

class Dijsktra:
	def __init__(self,nodes):
		self.graph=dt(lambda:[])
		self.nodes=nodes

	def addedge(self,u,v,d):
		self.graph[u].append((v,d))
		self.graph[v].append((u,d))

	def util(self,start):

		distance=[float('inf')]*(self.nodes)
		distance[start]=0
		priority=[(0,start)]


		while priority:

			d,u=heappop(priority)

			if d==distance[u]: #to only check min distance node in priority queue
				for v,d in self.graph[u]:
					if distance[u]+d<distance[v]:
						distance[v]=distance[u]+d
						heappush(priority,(distance[v],v))


		return distance


if __name__ == '__main__':
	
	g=Dijsktra(3)

	g.addedge(0,1,0.5)
	g.addedge(1,2,0.5)
	g.addedge(0,2,0.25)

	print(g.util(0))

