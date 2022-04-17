import sys
from collections import deque

input = sys.stdin.readline

n, m =map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    nodeA, nodeB = map(int,input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)
answer = 0
queue = deque()
for i in range(1,n+1):
    if not visited[i] :
        queue.append(i)
        visited[i] = True
        while queue :
            v = queue.popleft()
            for x in graph[v]:
                if not visited[x]:
                    queue.append(x)
                    visited[x]=True
        answer = answer + 1
print(answer)
        
