import sys
from collections import deque
input = sys.stdin.readline

nodeNumber , edgeNumber, startNode = map(int, input().split())
graph = [[]for row in range(nodeNumber+1)]
visited = [False] * (nodeNumber+1)
for i in range(1,edgeNumber+1):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)
    graph[nodeA].sort()
    graph[nodeB].sort()

    
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    
dfs(graph,startNode,visited)
visited = [False] * (nodeNumber+1)
print()
bfs(graph,startNode,visited)