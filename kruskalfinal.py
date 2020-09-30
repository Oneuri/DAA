class edge():
	def __init__(self,source,weight,dest):
		self.source=source
		self.weight=weight
		self.dest=dest
def returnwt(E):
	return E.weight
def findparent(node,parent):
	if parent[node]==node:
		return node
	return findparent(parent[node],parent)
def kruskals(edgesarray,n,E):
	edgesarray.sort(key=returnwt)
	counter=0      #keeps count of the number of edges taken
	i=0				# keeps track of the current edge
	parent=[i for i in range(n)]
	MST=[0 for x in range(n-1)]
	while(counter<n-1):
		current=edgesarray[i]
		sourceparent=findparent(current.source,parent)
		destparent=findparent(current.dest,parent)
		if sourceparent!=destparent:
			MST[counter]=current
			counter+=1
			parent[sourceparent]=destparent                      # parent[destparent]=sourceparent  also we can write...Doesnt matter
		i+=1

	for i in range(n-1):
		print(str(MST[i].source) +"\t"+str(MST[i].dest)+"\t"+str(MST[i].weight))
#main
n=5
E=7
graph= [ [0, 2, 0, 6, 0], 
         [2, 0, 3, 8, 5], 
         [0, 3, 0, 0, 7], 
         [6, 8, 0, 0, 9], 
         [0, 5, 7, 9, 0]] 
edgesarray=[]
for x in range(n):
	for y in range(n):
		if graph[x][y]!=0:
			newedge=edge(x,graph[x][y],y)
			edgesarray.append(newedge)
kruskals(edgesarray,n,E)
#main over
