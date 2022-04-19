import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(node,weights) :
    global maxWeight,maxVertex
    if maxWeight < weights :
        maxWeight = weights
        maxVertex = node
    if graph[node]:
        for v,w in graph[node]:
            if not visited[v]:
                visited[node] = True
                dfs(v,weights+w)
            
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
weightList = []
maxWeight=0
maxVertex=0
for _ in range(n-1):
    x,y,w = list(map(int,input().split()))
    graph[x].append((y,w))
    graph[y].append((x,w))

visited[1] = True
dfs(1,0)
visited = [False for _ in range(n+1)]
visited[maxVertex] = True
maxWeight = 0
dfs(maxVertex,maxWeight)
print(maxWeight)