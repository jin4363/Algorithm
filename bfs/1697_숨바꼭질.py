import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(N)
    while queue :
        v = queue.popleft()
        if v == K :
            return answer[v]
        for nx in (v-1, v+1, v*2):
            if 0<= nx <= max and answer[nx] == 0 :
                answer[nx] = answer[v]+1
                queue.append(nx)
        
N, K = map(int,input().split())
max = 10**5
answer = [0 for _ in range(max+1)]
            
print(bfs())