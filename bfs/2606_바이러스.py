import sys
from collections import deque

input = sys.stdin.readline

nodeN = int(input())
edgeN = int(input())
graph = [[]for row in range(nodeN+1)]
visited = [False for _ in range(nodeN+1)]
for i in range(edgeN):
    nodeA , nodeB = map(int,input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

def bfs(startNode):
    queue = deque([startNode])
    visited[startNode]=True
    count = 0
    while queue:
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i]=True
                count = count+1
    return count

print(bfs(1))
            
        