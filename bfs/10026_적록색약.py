
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

visited = []
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(N):
    graph.append(list(input().strip()))

def bfs(xPos,yPos,color):
    global visited
    queue = deque()
    queue.append((xPos,yPos))
    visited[xPos][yPos] = True
    while queue :
        x,y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if not visited[nx][ny] and graph[nx][ny] == color:
                    queue.append((nx,ny))
                    visited[nx][ny] =True
def RG_bfs(xPos,yPos):
    global visited
    queue = deque()
    queue.append((xPos,yPos))
    visited[xPos][yPos] = True
    while queue :
        x,y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if not visited[nx][ny] and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                    queue.append((nx,ny))
                    visited[nx][ny] =True
def R_G_B():
    global visited
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'R' and not visited[i][j]:
                bfs(i,j,'R')
                count += 1
            if graph[i][j] == 'G' and not visited[i][j]:
                bfs(i,j,'G')
                count += 1
            if graph[i][j] == 'B' and not visited[i][j]:
                bfs(i,j,'B')
                count += 1
    return count

def RG_B():
    global visited
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if (graph[i][j] == 'R' or graph[i][j] == 'G') and not visited[i][j]:
                RG_bfs(i,j)
                count += 1
            if graph[i][j] == 'B' and not visited[i][j]:
                bfs(i,j,'B')
                count += 1
    return count
            
print('%d %d' %(R_G_B(),RG_B()))

