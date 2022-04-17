import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
M, N, K = 0, 0 ,0
def bfs(x,y,visited,graph):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue :
        x,y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N :
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                
for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[0 for _ in range(N)]for _ in range(M)]
    visited = [[False for _ in range(N)]for _ in range(M)]
    minWorm = 0
    for _ in range(K):
        x , y = map(int,input().split())
        graph[x][y] = 1
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i,j,visited,graph)
                minWorm = minWorm + 1
    print(minWorm)
                