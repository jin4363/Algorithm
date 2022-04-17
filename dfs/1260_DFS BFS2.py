import sys
from collections import deque
input = sys.stdin.readline

nodeNumber, edgeNumber , startNode = map(int,input().split())
graph = [[]for row in range(nodeNumber+1)]
dfsVisited = [False] * (nodeNumber+1)
bfsVisited = [False] * (nodeNumber+1)
for i in range(edgeNumber):
    nodeA, nodeB = map(int,input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)
    graph[nodeA].sort()
    graph[nodeB].sort()
    
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i] :
            dfs(graph,i,visited)
            
def bfs(graph,v,visited):
    queue = deque([v])
    visited[v]=True
    while queue:
        i = queue.popleft()
        print(i,end=' ')
        for node in graph[i]:
            if not visited[node]:
                queue.append(node)
                visited[node]=True
    
dfs(graph,startNode,dfsVisited)
print()
bfs(graph,startNode,bfsVisited)
        
        
    