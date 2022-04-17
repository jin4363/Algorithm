import sys
from collections import deque

input = sys.stdin.readline


dx = [-1,1,0,0,-1,+1,-1,+1]
dy = [0,0,-1,1,-1,-1,+1,+1]

def bfs(i,j,w,h):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue :
        x,y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True 
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    graph = []
    visited = [[False for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        graph.append(list(map(int,input().split())) )
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j] :
                bfs(i,j,w,h)
                count = count + 1
    print(count)