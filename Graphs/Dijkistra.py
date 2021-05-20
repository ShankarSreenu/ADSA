import sys
infinity = sys.maxsize
graph={}
      
def add_edge(u,v,w):
    if graph.get(u):
        nodes=graph.get(u)
        nodes.append([v,w])
        graph[u]=nodes
    else:
        graph[u]=[[v,w]]


def dijkistra(graph):
    n=4
    visted=[0 for i in range(0,n+1)]
    d=[infinity for i in range(0,n+1)]
    edge=graph.get(1)
    for node in edge:
        d[node[0]]=node[1]
    count=0
    d[1]=0
    while count<len(d):
        print("*")
        mini=infinity
        index=0
        for i in range(0,len(d)):
            if mini>d[i] and visted[i]==0:
                index=i
                mini=d[i]
        visted[index]=1
        edges=graph.get(index)
        if edges:
            for nodes in edges:
                
                if nodes[1]+d[index]<d[nodes[0]]:
                    d[nodes[0]]=nodes[1]+d[index]
        count=count+1
    print(d)
    


#n no of nodes
add_edge(1,2,1)
add_edge(1,3,5)
add_edge(1,4,0)
add_edge(2,4,2)
add_edge(4,3,0)
add_edge(3,1,2)
dijkistra(graph)
