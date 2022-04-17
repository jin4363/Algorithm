import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

graph = []
visited  =[[False for col in range(N) ]for row in range(N)]
for i in range(N):
    graph.append(list(map(int,input().strip())))

answer=[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    homeCount = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >=N or ny <0 or ny >=N:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False :
                queue.append((nx,ny))
                visited[nx][ny] = True
                homeCount = homeCount + 1
    answer.append(homeCount)
            
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] ==1:
            bfs(i,j)
            
answer.sort()
print(len(answer))
for number in answer:
    print(number)





