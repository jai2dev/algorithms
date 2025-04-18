'''
1. node class
	1. nodeId
	2.nodeName
	3.nodeWeight

2. weighted round robin class
	variables
	1. storing nodes
	2. curNode
	methods
	1. aquireNode
	2.freeNode
	3.addNode
	4.deleteNode
	5. releaseNode
'''
import threading

class Node:
	def __init__(self,nodeId,nodeName,nodeWeight):
		self.id=nodeId
		self.name=nodeName
		self.weight=nodeWeight
		self.lock=threading.Lock()

class WeightedRoundRobin:
	def __init__(self,nodes):
		self.nodes=list(nodes)
		self.curNode=0
		self.requestToNode={}
		self.global_lock = threading.Lock()
		self.length=len(nodes)


	def addNode(self,node):
		with self.global_lock:
			self.nodes.append(node)
			self.length+=1

	def removeNode(self,node):
		with self.global_lock:
			self.nodes.remove(node)
			self.length-=1
			self.curNode=0


	def aquireNode(self,request):
		try:
			with self.global_lock:
				node=self.nodes[self.curNode%self.length]
				while node.weight==0:
					self.curNode+=1
					node=self.nodes[self.curNode]
				node.weight-=1
				acquired=node.lock.acquire(blocking=False)
                if acquired:
                    # Schedule the release of the node after 30 seconds
                    timer = threading.Timer(30, self.releaseNode, [node])
                    timer.start()
                    return node

		except Exception as e:
			raise "No Server Found"


	def releaseNode(self):
		try:
			if node.lock.locked():
				node.lock.release()
			
		except Exception as e:
			raise "No Server Found"

