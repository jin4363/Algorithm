import sys
import pprint
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
visited=[]
maxHeight = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] > maxHeight :
            maxHeight = graph[i][j]

def bfs(xPos,yPos,h):
    global visited
    queue = deque()
    queue.append((xPos,yPos))
    visited[xPos][yPos] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] > h :
                    queue.append((nx,ny))
                    visited[nx][ny] =True

for h in range(maxHeight):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and not visited[i][j]:
                bfs(i,j,h)
                count = count +1
    answer = max(answer,count)

      
print(answer)

    
            