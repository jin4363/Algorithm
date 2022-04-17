import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(x,y):
    #도착지점 도착시 1리턴
    if x == M-1 and y == N-1 :
        return 1
    #이미 방문한적 있으면 그위치 경우의수 리턴
    if dp[x][y] != -1 :
        return dp[x][y]
    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[x][y] > graph[nx][ny]:
            ways += dfs(nx,ny)
    dp[x][y] = ways
    return dp[x][y]

M,N = map(int,input().strip().split()) #500이하 자연수 M,N이라 메모이제이션 필요
graph = []
for i in range(M):
    graph.append(list(map(int,input().strip().split())))
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]



print(dfs(0,0))