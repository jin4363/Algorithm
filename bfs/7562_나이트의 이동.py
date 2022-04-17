import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

size = 0
nowPosX, nowPosY = 0,0
goalPosX, goalPosY = 0,0

dx = [0,-2,-1,1,2,2,1,-1,-2]
dy = [0,1,2,2,1,-1,-2,-2,-1]
graph = []

def bfs(startX,startY,size,goalPosX,goalPosY,graph):
    queue = deque()
    queue.append((startX,startY))
    graph[startX][startY] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < size and 0 <= ny < size :
                if nx == goalPosX and ny == goalPosY :
                    return graph[x][y]
                if graph[nx][ny] == 0 :
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
for _ in range(T):
    size = int(input())
    result = 0
    nowPosX, nowPosY = map(int,input().strip().split())
    goalPosX, goalPosY = map(int,input().strip().split())
    graph = [[0 for _ in range(size)] for _ in range(size)]
    result=bfs(nowPosX,nowPosY,size,goalPosX,goalPosY,graph)
    print(result)