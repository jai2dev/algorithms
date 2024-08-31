class Node:
	def __init__(self, val):
		self.val=val
		self.left=None
		self.right=None
		
class MakeTree():
	def __init__(self,nodes):
		self.nodes=nodes

	def makeTree(self,u=0):
		if u>=len(nodes):return
		cNode=Node(self.nodes[u])
		cNode.left=self.makeTree(2*u+1)
		cNode.right=self.makeTree(2*u+2)
		return cNode


def morrisTraversal(root):
	ans=[]
	while root:
		if not root.left:
			ans.append(root.val)
			root=root.right
			continue
		temp=root.left
		while temp.right and temp.right!=root:
			temp=temp.right
		if temp.right:
			ans.append(root.val)
			root=root.right
			temp.right=None
		else:
			temp.right=root
			root=root.left
	return ans


if __name__ == '__main__':
	nodes=[1,2,3,4,5,6]
	newTree=MakeTree(nodes)
	print(morrisTraversal(newTree.makeTree()))

	

