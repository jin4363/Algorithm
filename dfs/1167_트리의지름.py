import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node,weights):
    global visited,graph,maxWeight,maxVertex
    if maxWeight < weights :
        maxWeight = weights
        maxVertex = node
    if graph[node]:
        for vertex,weight in graph[node]:
            if not visited[vertex] :
                visited[vertex] = True
                dfs(vertex,weights + weight)
            


V = int(input())
graph=[[]for _ in range(V+1)]
maxWeight = 0
maxVertex = 0
for _ in range(V):
    tempInput = list(map(int,input().strip().split()))
    nodeA = tempInput[0]
    for i in range(1,int((len(tempInput)-2)+1),2):
        nodeB = tempInput[i]
        w = tempInput[i+1]
        graph[nodeA].append((nodeB,w))
        graph[nodeB].append((nodeA,w))


visited = [False for _ in range(V+1)]
visited[1] = True
dfs(1,0)
visited = [False for _ in range(V+1)]
visited[maxVertex] = True
maxWeight = 0
dfs(maxVertex,maxWeight)
print(maxWeight)