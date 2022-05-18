import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue=deque([])
def find_start():
    rx,ry,bx,by = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'R':
                rx,ry = i,j
            elif maps[i][j] == 'B':
                bx,by = i,j
    queue.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by] = True
def move(x,y,dx,dy):
    cnt=0
    #다음이 벽이거나 현재가 구멍일때까지
    while maps[x+dx][y+dy] != '#' and maps[x][y] != 'O' :
        x +=dx
        y +=dy
        cnt +=1
    return x,y,cnt

def bfs():
    find_start() #시작지점 찾고 큐에 넣기
    while queue:
        rx,ry,bx,by,depth = queue.popleft()
        if depth > 10: #10회 이내까지만 //실패조건
            break
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])
            if maps[nbx][nby] != 'O': #실패 조건이 아니면
                if maps[nrx][nry] == 'O': #성공조건이면
                    print(depth)
                    return
                #겹칠시 이동칸이 많은 구슬 한칸 후퇴
                if nrx == nbx and nry == nby :
                    if rcnt > bcnt :
                        nrx -= dx[i]
                        nry -= dy[i]
                    else :
                        nbx -= dx[i]
                        nby -= dy[i]
                #기울인후(bfs탐색후), 방문 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    #방문 안햇으면 체크후 큐에 추가
                    visited[nrx][nry][nbx][nby]=True
                    queue.append((nrx,nry,nbx,nby,depth+1))
    print(-1)
bfs()