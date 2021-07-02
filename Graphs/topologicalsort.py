def topologicalsort(graph):
    visited={}
    sorted=[]
    for key,val in graph.items():
        if key not in visited:
            visited[key]=True
            stack=[key]
            while stack:
                reach=False
                top=stack[-1]
                for nhb in graph[top]:
                    if nhb not in visited:
                        stack.append(nhb)
                        visited[nhb]=True
                        reach=True
                
                if reach==False:
                    node=stack.pop()
                    sorted.insert(0,node)
    return sorted

graph={2:[1],3:[2],1:[]}
res=topologicalsort(graph)
print(res)








