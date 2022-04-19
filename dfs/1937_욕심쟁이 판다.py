import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global ans
    #이미 방문한적 있으면 그위치 경우의수 리턴
    if dp[x][y] != -1 :
        return dp[x][y]
    ways = 1
    maxRes = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            maxRes = max(dfs(nx,ny),maxRes)
    dp[x][y] = ways + maxRes
    ans = max(ans,dp[x][y])
    return dp[x][y]
n = int(input())
graph = []
dp = [[-1]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
for _ in range(n):
    graph.append(list(map(int,input().strip().split())))

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1 :
            dfs(i,j)
print(ans)
