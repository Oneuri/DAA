import sys


class Graph:
	def __init__(self, vertices): 
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 


	def minimumkey(self,key,mstset):
		min=sys.maxsize
		for i in range(self.V):
			if key[i]< min and mstset[i]==False:                   #if key is less than previous key AND NODE IS NOT VISITED
				min=key[i]
				min_index=i
		return min_index
	def printMST(self, parent): 
		print("Edge \t Weight")
		for x in range(1,self.V):
			print(parent[x], "-", x, "\t", self.graph[x][parent[x]]) 

	def prims(self):
		key=[sys.maxsize]*self.V
		parent=[None]*self.V
		key[0]=0
		mstset=[False]* self.V
		parent[0]= -1



		for x in range(self.V):
			u=self.minimumkey(key,mstset)
			mstset[u]=True
			for v in range(self.V):
				if self.graph[u][v]>0 and mstset[v]==False and key[v]>self.graph[u][v]:
					key[v]=self.graph[u][v]
					parent[v]=u
		self.printMST(parent)

g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.prims(); 
