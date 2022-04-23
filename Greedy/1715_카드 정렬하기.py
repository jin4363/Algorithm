import sys
import heapq
input =sys.stdin.readline
t = int(input())
num = []
for _ in range(t):
    heapq.heappush(num,int(input()))
ans = 0
while len(num) > 1 :
    cardA = heapq.heappop(num)
    cardB = heapq.heappop(num)
    ans += cardA + cardB
    heapq.heappush(num,cardA+cardB)
print(ans)