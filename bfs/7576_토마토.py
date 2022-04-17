import sys
from collections import deque

input = sys.stdin.readline

col , row = map(int,input().split())
visited = [[False for _ in range(col)]for _ in range(row)]

graph = []
for i in range(row) :
    graph.append(list(map(int,input().split())))
    

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    day=0
    queue = deque()
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 :
                queue.append((i,j))
                
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >=col:
                continue
            if graph[nx][ny] == 0  :
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
                day = graph[nx][ny]
    return day-1

def zeroFind(row,col):
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0 :
                return True
    return False
    
day = bfs()
if zeroFind(row,col) :
    print(-1)
elif day == -1:
    print(0)
else:
    print(day)

        
        
            