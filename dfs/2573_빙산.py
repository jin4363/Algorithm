import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def melt():
    global r,c,graph
    meltList=[]
    waterCount=0
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 :
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        if graph[nx][ny] == 0 :
                            waterCount +=1
                meltList.append((i,j,waterCount))
                waterCount=0
    while meltList :
        x,y,cnt = meltList.pop()
        graph[x][y] -= cnt
        if graph[x][y] < 0 :
            graph[x][y] = 0
def dfs(x,y):
    global r,c,visited
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny< c :
            if not visited[nx][ny] and graph[nx][ny] != 0:
                dfs(nx,ny)
            
r,c = map(int,input().split())
year = 0
count =0
graph = []
visited = [[False]*c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(r):
    graph.append(list(map(int,input().strip().split())))
while True :

    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0 and not visited[i][j] :
                dfs(i,j)
                count += 1
    if count >= 2 or count == 0:
        break
    else : 
        melt()
        year +=1
        count=0
        visited = [[False]*c for _ in range(r)]

if count >= 2 :
    print(year)
else:
    print(0)