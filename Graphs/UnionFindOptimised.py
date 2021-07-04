
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



input=[[0,1],[1,2],[2,3],[3,0]]
V=4
E=4
graph={i:[] for i in range(V)}
parent=[-1]*V
rank=[1]*V
for i in range(0,E):
    u,v=input[i]
    graph[u]=graph.get(u)+[v]
    #graph[v]=graph.get(v)+[u]

for key,val in graph.items():
    for nhb in val:
        x=find(key,parent)
        y=find(nhb,parent)
        if x!=y:
            union_by_rank(key,nhb,parent,rank)
        else:
            print("cycle")
            break
        
print(rank,parent)
        

