import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().strip().split())
packList=[]
singleList = []
for _ in range(m):
    #패키지는 줄 6개 가격
    packagePrice, singlePrice = map(int,input().strip().split())
    heapq.heappush(packList,packagePrice)
    heapq.heappush(singleList,singlePrice)
ans = 0 

if packList[0] <= singleList[0]*6.0 :
    ans = packList[0] * (n//6) + singleList[0] * (n%6)
    if packList[0] < singleList[0] * (n%6) :
        ans = packList[0] * (n//6 + 1)
else :
    ans = singleList[0] * n
        
print(ans)