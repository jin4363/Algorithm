import sys
from collections import deque

input = sys.stdin.readline
answer = 0
def wall(cnt):
    global M,N
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 :
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0
def bfs():
    copy= [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    count = 0
    global answer, funcCount
    for i in range(N):
        for j in range(M):
            copy[i][j] = graph[i][j]
    for i in range(N) :
        for j in range(M):
            if copy[i][j] == 2:
                queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if N <= nx or nx < 0 or M <=ny or ny < 0:
                continue
            if copy[nx][ny] == 0 :
                queue.append((nx,ny))
                copy[nx][ny] = 2
    for i in range(N) :
        for j in range(M):
            if copy[i][j] == 0:
                count = count + 1
    answer= max(answer,count)

       
N, M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
wall(0)
print(answer)