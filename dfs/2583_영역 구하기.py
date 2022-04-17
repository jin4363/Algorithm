import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
M,N,K = map(int,input().split())

graph = [[0 for _ in range(N)]for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ansList=[]
def dfs(x,y,depth):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N :
            if graph[nx][ny] == 0 :
                depth = max(dfs(nx,ny,depth+1),depth)
    return depth
for _ in range(K):
    bottomX , bottomY , topX , topY = map(int,input().split())
    for i in range(bottomY,topY):
        for j in range(bottomX,topX):
            graph[i][j] = -1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            ansList.append(dfs(i,j,1))

ansList.sort()
print(len(ansList))
for i in ansList:
    print(i,end=' ')