def belmenford(V,edges):
    INT_MAX=float('inf')
    dist=[INT_MAX]*V
    dist[0]=0
    for i in range(0,V-1):
        for val in edges:
            u,v,w=val
            if dist[u]!=INT_MAX and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
    for val in edges:
        u,v,w=val
        if dist[u]!=INT_MAX and dist[u]+w<dist[v]:
            print("Negative Cycle")
            break
    return dist

E=[[0,1,10],[1,2,9],[2,3,3],[1,3,-10]]
V=4
ans=belmenford(V,E)
print(ans)
