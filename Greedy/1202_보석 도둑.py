
import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().strip().split())
gem = []
bag = []
for _ in range(n):
    m,v = map(int,input().strip().split())
    gem.append([m,v])
for _ in range(k):
    bag.append(int(input()))    
bag.sort()
gem.sort()
ans = 0
temp = []
for w in bag:
    while gem and w >= gem[0][0]:
        heapq.heappush(temp,-gem[0][1]) #max heap으로 -붙여서 사용해서 최대 가치인것 푸시 
        heapq.heappop(gem)
    if temp :
        ans += heapq.heappop(temp)
    elif not gem :
        break
print(-ans)