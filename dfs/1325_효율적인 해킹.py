
#dfs는 계속 메모리 초과
# import sys
# input =sys.stdin.readline
# def dfs(v):
#     global graph,visited
#     if graph[v] :
#         for i in graph[v]:
#             if visited[i] == 0:
#                 visited[v] += dfs(i)
#             else :
#                 visited[v] += visited[i]
#         visited[v] += 1
#         return visited[v]
#     else :
#         return 1
# for _ in range(m):
#     nodeA,nodeB = map(int,input().strip().split())
#     graph[nodeB].append(nodeA)

# for i in range(1,n+1):
#     if visited[i] == 0 :
#         visited[i] = dfs(i)
# maxNum = max(visited)
# for i in range(1,n+1) :
#     if visited[i] == maxNum :
#         ans.append(i)
# ans.sort()
# for i in ans:
#     print(i,end=' ')
# n,m = map(int,input().strip().split())
import sys
from collections import deque
input =sys.stdin.readline

def bfs(v) :
    global graph,visited,cnt
    queue = deque([v])
    while queue :
        node = queue.popleft()
        if graph[node] :
            for i in graph[node] :
                if not visited[i] :
                    visited[i] = True
                    queue.append(i)
                    cnt +=1
                    
n,m = map(int,input().strip().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    nodeA,nodeB = map(int,input().strip().split())
    graph[nodeB].append(nodeA)
ans = []
maxNum = 0
for i in range(1,n+1) :
    visited = [False for _ in range(n+1)]
    cnt =0
    if not visited[i]  :
        visited[i] = True
        bfs(i)
    if cnt > maxNum:
        maxNum = cnt
        ans = [i]
    elif cnt == maxNum :
        ans.append(i)
print(*ans)