from disjointset import *
from operator import itemgetter

class graph:


    def __init__(self,list,node):

        self.list=list
        self.node=node
        self.addedge=[]
        self.node_list=[]


        self.sorted_edge=sorted(self.list,key=itemgetter(2))

        # print(self.sorted_edge)

    def kruskal(self):

        ds=DisjointSets()
        for i in self.node:
            node=ds.makeset(i)
            self.node_list.append(node)
            # print("***",i.rank)
        # print("^^^",self.node_list)
        cost=0
        for edge in self.sorted_edge:
            u=self.node_list[edge[0]]
            v=self.node_list[edge[1]]
            w=edge[2]
            # print(u,v,w)
            if(ds.findset(u)!=ds.findset(v)):
                self.addedge.append([u,v,w])
                cost=cost+w
                ds.union(u,v)
        print("Nodes in kruskal along with their weights are:")
        for u,v,w in self.addedge:
            print(str(u),str(v),w,sep=" ")
        print("Total min cost is")
        print(cost)
        # print(self.addedge)




    






def main():
    G=[]
    linecount=0
    node=[]
    file=open("input1.txt","r")
    for line in file:
        first=True
        for edge in line.split(" "):
            if first==True:
                first=False
            else:
                v,weight=edge.split(",")
                G.append((linecount,int(v),int(weight)))
        node.append(linecount)    
        linecount+=1



    # print(node)
    file.close()
    print(G)
    g=graph(G,node)
    g.kruskal()
   




if __name__ == '__main__':
    main()