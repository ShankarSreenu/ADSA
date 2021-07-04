
#worst case it can go to order(n)
def find_normal(u,parent):
    if parent[u]==-1:
        return u
    return find(parent[u],parent)

#path compressed
def find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=find(parent[u],parent)
    return parent[u]

#union by rank
def union_by_rank(u,v,parent,rank):
    x=find(u,parent)
    y=find(v,parent)
    if x!=y:
        if x<y:
            parent[x]=y
            rank[x]=rank[x]+rank[y]
        else:
            parent[y]=x
            rank[y]=rank[y]+rank[x]
    return

def union(u,v,parent):
    x=find(u,parent)
    y=find(v,parent)
    if x!=y:
        parent[y]=x
    return



input=[[0,1,2],[1,2,3],[10,2,1]]
V=4
E=3
graph={i:[] for i in range(8)}
parent=[-1]*V
rank=[1]*V
min_cost=0
for i in range(0,E):
    w,u,v=input[i]
    graph[u]=graph.get(u)+[(w,v)]
    #graph[v]=graph.get(v)+[(w,u)]

graph=list(graph.items())
sorted(graph,key=lambda x:x[0])
for x in graph:
    key,val=x
    for nhb in val:
        x=find(key,parent)
        y=find(nhb[1],parent)
        if x!=y:
            union_by_rank(key,nhb[1],parent,rank)
            min_cost=min_cost+nhb[0]
        else:
            print("cycle")
            break
        
print(min_cost)
        

