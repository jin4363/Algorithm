import sys
input = sys.stdin.readline
n = int(input())
distance = list(map(int,input().strip().split()))
price = list(map(int,input().strip().split()))
totalDist = sum(distance)
ans = distance[0] * price[0]
moveDist = distance[0]
nowPrice = price[0]
idx=1

while True :
    if totalDist - moveDist == 0 :
        break
    if nowPrice < price[idx] :
        ans += distance[idx] * nowPrice
        moveDist += distance[idx]
    else :
        nowPrice = price[idx]
        ans += distance[idx] * nowPrice
        moveDist += distance[idx]
    idx +=1 
print(ans)