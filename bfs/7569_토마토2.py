import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().strip().split()) #가로 세로 높이

graph = []


for i in range(H):
    tempArr = []
    for j in range(N):
        tempArr.append(list(map(int,input().strip().split())))
    graph.append(tempArr)
   
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]  

def bfs():
    global graph
    queue = deque()
    day=0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1 :
                    queue.append((i,j,k))
    while queue :
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (H > nx >= 0 and N > ny >= 0 and M > nz >=0):
                if  graph[nx][ny][nz]==0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx,ny,nz))
                
def find():
    global graph,day
    for i in graph:
        for j in i:
            for k in j:
                if k==0:
                    return True
            day=max(day,max(j))
bfs()
day=0
if find():
    print(-1)
else :
    print(day-1)
