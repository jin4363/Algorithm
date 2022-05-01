
import sys

input = sys.stdin.readline

def solve(i,j):
    global r,c,visited,mapList
    if j == c - 1:
        return True
    for k in range(3):
        nx = i + dx[k]
        ny = j + 1
        if 0<=nx<r and 0<=ny<c and mapList[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            if solve(nx,ny):
                return True
    return False
            


r,c = map(int,input().split())
visited = [[False ] * c for _ in range(r)]
mapList = []
for i in range(r):
    mapList.append(list(map(str,input().strip())))
dx = [-1,0,1]
cnt = 0 
for i in range(r) :
    if mapList[i][0] == '.':
        if solve(i,0):
            cnt +=1
print(cnt)