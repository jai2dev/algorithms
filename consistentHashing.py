import sys,traceback,hashlib,bisect,re
from sortedcontainers import SortedList

class Node:
	def __init__(self,nodeId,name,weight):
		self.id=nodeId
		self.name=name
		self.weight=weight #relative load that this node can handle, the more the weight more the number of virtual nodes on the hash ring


class ConsistentHashing:
	def __init__(self):
		self.nodes=SortedList()
		self.nodeIdToNodes={}
		self.nodeToId=defaultdict(lambda:[])

	def hash(self,request, limit=4294967295):
        keyHash=hashlib,sha512(request.encode())
        key=int.from_bytes(keyHash.digest(),"big")%limit
        return key

    def deleteNode(self,node):
    	'''
    	Function that could be used to remove the node from the cluster
    	'''
    	return True

    def addNode(self,node):
      	'''
    	Function that could be used to add the node from the cluster
    	'''
    	return True

	def getNode(self,request):
		requestId=self.hash(request)
		nodeIdIndex=self.nodes.bisect_left(requestId)
		if nodeIdIndex<len(self.nodes):
			return self.nodeIdToNodes[self.nodes[nodeIdIndex]]
		return self.nodeIdToNodes[self.nodes[0]]

	def addNode(self,node):
		nodeId=node.id
		for i in range(1,node.weight+1):
			virtualNodeId=self.hash(nodeId+i)
			self.nodeIdToNodes[virtualNodeId]=node
			self.node.add(virtualNodeId)
			self.nodeToId[node].append(virtualNodeId)
		self.addNode(node)
		return "Successfully Added Node"

	def removeNode(self,node):
		for  nodeId in self.nodeToId[node]:
			del self.nodeIdToNodes[nodeId]
			self.nodes.remove(nodeId)
		del self.nodeToId[node]
		self.deleteNode(node)
		return "Successfully removed the Node"




class LoadBalancer:
	def __init__(self):
		self.algorithm=ConsistentHashing()


	def addNode(self,node):
		self.algorithm.addNode(node)

	def removeNode(self,node):
		self.algorithm.removeNode(node)

	def getNode(self,request):
		return self.algorithm(request)



