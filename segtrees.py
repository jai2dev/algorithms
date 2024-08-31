from collections import defaultdict as dt
from math import ceil,log2
import sys
import os




class SegmentTree:
	
	def __init__(self, arr, nodes):
		
		self.arr = arr
		self.nodes=nodes



	def constructTree_sum(self,st,end,cur):

		if st==end:
			self.segment[cur]=self.arr[st]

			return self.segment[cur]


		middle=st+(end-st)//2


		self.segment[cur]= self.constructTree_sum(st,middle,2*cur+1)+self.constructTree_sum(middle+1,end,2*cur+2)

		return self.segment[cur]


	def constructTree_min(self,st,end,cur):

		if st==end:
			self.segment[cur]=(self.arr[st],1)

			return self.segment[cur]


		middle=st+(end-st)//2

		a,b=self.constructTree_min(st,middle,2*cur+1),self.constructTree_min(middle+1,end,2*cur+2)
		if a[0]==b[0]:
			self.segment[cur]= (a[0],a[1]+b[1])

		elif a[0]<b[0]:
			self.segment[cur]=a
		else:
			self.segment[cur]=b

		return self.segment[cur]


	def constructTree_max(self,st,end,cur):

		if st==end:
			self.segment[cur]=self.arr[st]

			return self.segment[cur]


		middle=st+(end-st)//2


		self.segment[cur]= max(self.constructTree_max(st,middle,2*cur+1),self.constructTree_max(middle+1,end,2*cur+2))

		return self.segment[cur]


	def makeTree(self,type='sum'):

		segmentLength=ceil(log2(self.nodes))

		


		if type=='sum':
			self.segment=[0]*(2*2**segmentLength-1)

			self.constructTree_sum(0,self.nodes-1,0)

		elif type=='min':
			self.segment=[(0,0)]*(2*2**segmentLength-1)

			self.constructTree_min(0,self.nodes-1,0)

		elif type=='max':
			self.segment=[0]*(2*2**segmentLength-1)
			self.constructTree_max(0,self.nodes-1,0)


		return self.segment



	def update_util_sum(self,st,end,index,cur,diff):




		if st<=index<=end:
			self.segment[cur]+=diff


			if st!=end:
				middle=st+(end-st)//2

				

				self.update_util_sum(st,middle,index,2*cur+1,diff)
				self.update_util_sum(middle+1,end,index,2*cur+2,diff)


	def update_util_min(self,st,end,index,cur,new):




		if st<=index<=end:
			

			if st==end:
				self.segment[cur]=(new,1)


			else:
				middle=st+(end-st)//2

				
				if st<=index<=middle:
					self.update_util_min(st,middle,index,2*cur+1,new)
				else:
					self.update_util_min(middle+1,end,index,2*cur+2,new)

				a,b=self.segment[2*cur+1],self.segment[2*cur+2]
				if a[0]==b[0]:

					self.segment[cur]=(a[0],a[1]+b[1])

				elif a[0]<b[0]:
					self.segment[cur]=a

				else:
					self.segment[cur]=b


	def update_util_max(self,st,end,index,cur,new):




		if st<=index<=end:
			# self.segment[cur]=max(new,self.segment[cur])

			if st==end:
				self.segment[cur]=new
			else:
				middle=st+(end-st)//2

				
				if st<=index<=middle:
					self.update_util_max(st,middle,index,2*cur+1,new)
				else:
					self.update_util_max(middle+1,end,index,2*cur+2,new)


				self.segment[cur]=max(self.segment[2*cur+1],self.segment[2*cur+2])

	def update(self,index,new,type='sum'):


		if -1<index<self.nodes:
			

			if type=='sum':
				diff=new-self.arr[index]
				arr[index]=new
				self.update_util(0,self.nodes-1,index,0,diff)

			elif type=='min':

				arr[index]=new
				self.update_util_min(0,self.nodes-1,index,0,new)

			elif type=='max':

				arr[index]=new
				self.update_util_max(0,self,nodes-1,index,0,new)


	def sum_util(self,st,end,l,r,cur):

		if l<=st and end<=r:
			return self.segment[cur]

		if l>end or r<st:
			return 0

		middle= st+(end-st)//2

		return self.sum_util(st,middle,l,r,2*cur+1)+self.sum_util(middle+1,end,l,r,2*cur+2)


	def min_util(self,st,end,l,r,cur):

		if l<=st and end<=r:
			return self.segment[cur]

		if l>end or r<st:
			return (sys.maxsize,0)

		middle= st+(end-st)//2

		a,b=self.min_util(st,middle,l,r,2*cur+1),self.min_util(middle+1,end,l,r,2*cur+2)

		if a[0]==b[0]:

			return (a[0],b[1]+a[1])
		elif a[0]<b[0]:
			return a

		else:
			return b


	def max_util(self,st,end,l,r,cur):

		if l<=st and end<=r:
			return self.segment[cur]

		if l>end or r<st:
			return -1

		middle= st+(end-st)//2

		return max(self.max_util(st,middle,l,r,2*cur+1),self.max_util(middle+1,end,l,r,2*cur+2))


	def range_query(self,l,r,type='sum'):
		if l>-1 and r<self.nodes:


			if type=='sum':

				return self.sum_util(0,self.nodes-1,l,r,0)

			elif type=='min':
				return self.min_util(0,self.nodes-1,l,r,0)

			elif type=='max':
				return self.max_util(0,self.nodes-1,l,r,0)



if __name__ == '__main__':
	# arr=[5]

	# segment_tree=SegmentTree(arr,1)


	# use the queries with type variable

	# example make_Tree(type)
	# example update(index,value,type)
	# example range_query(l,r,type)
	# print the tree segment_tree.segment


	n,m=list(map(int,input().split()))

	arr=list(map(int,input().split()))


	segment_tree=SegmentTree(arr,n)
	segment_tree.makeTree('min')

	# print(segment_tree.segment)

	for _ in range(m):

		t,a,b=list(map(int,input().split()))

		if t==1:
			segment_tree.update(a,b,'min')
		else:
			ans=segment_tree.range_query(a,b-1,'min')
			print(ans[0], ans[1])



