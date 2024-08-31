class Node:
    def __init__(self,x):
        self.val = x
        self.parent = self
        self.rank = 0

    def __str__(self):
        return str(self.val)

class DisjointSets: 

    def makeset(self,x):
        return Node(x)

    def findset(self,p):
        if p.parent!=p:
            p.parent=self.findset(p.parent)
        return p.parent


    def union(self,x,y):

        rootx=self.findset(x)
        # print("%%%%",rootx)
        # print("$$$",rootx.rank)
        rooty=self.findset(y)
        # print("(((",rooty)
        # print("$$$",rootx.rank)

        if(rootx==rooty):
            return

        if(rootx.rank>rooty.rank):
            rooty.parent=rootx


        elif(rootx.rank<rooty.rank):
            rootx.parent=rooty

        else:
            rootx.parent=rooty
            rooty.rank=rooty.rank+1


   
   
def main():
    ds = DisjointSets()
    
    nodes = []
    for i in range(10):
        node = ds.makeset(i)
        nodes.append(node)
    print("%%%",nodes)

    

    print(ds.findset(nodes[0]))
    ds.union(nodes[0],nodes[1])
    print(ds.findset(nodes[0]))

    ds.union(nodes[0],nodes[2])
    print(ds.findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''

if __name__ == '__main__':
    main()