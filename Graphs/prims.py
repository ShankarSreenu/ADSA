#User function Template for python3
import heapq as hq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        graph={i:[] for i in range(0,V)}
        for i in range(0,len(adj)):
            for val in adj[i]:
                node,w=val
                graph[i]=graph.get(i)+[(w,node)]
                #graph[node]=graph.get(node)+[(w,i)]
        cost=0
        heap=[]
        visited={}
        hq.heappush(heap,[0,0])
        while len(heap)>0:
            mincost,node=hq.heappop(heap)
            if node in visited:
                continue
            visited[node]=True
            cost=cost+mincost
            for nhb in graph[node]:
                if nhb not in visited:
                    hq.heappush(heap,[nhb[0],nhb[1]])
                    visited[nhb]=True
        return cost
                
