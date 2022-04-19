import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
m,n = map(int,input().split())
def dfs(x,y):
    global graph,m,n,visited
    
    if graph[x][y] == 0 :
        visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n :
            if not visited[nx][ny] :
                if graph[nx][ny] >= 1:
                    graph[nx][ny] +=1
                else :
                    dfs(nx,ny)

graph = []
visited = []
for _ in range(m) :
    graph.append(list(map(int,input().strip().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
hour=0
while True :
    visited = [[False for _ in range(n)] for _ in range(m)]
    dfs(0,0)
    find = False
    for i in range(m) :
        for j in range(n) :
            if graph[i][j] >= 3:
                graph[i][j] = 0
                find = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if find :
        hour += 1
    else :
        break
print(hour)
                
        
            