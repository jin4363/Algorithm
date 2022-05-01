import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
timeList = []
for _ in range(n):
    timeList.append(list(map(int,input().split())))
timeList.sort(key=lambda x : x[0])
room = []
heapq.heappush(room,timeList[0][1])

for i in range(1,n):
    if timeList[i][0] < room[0] :
        heapq.heappush(room,timeList[i][1])
    else :
        heapq.heappop(room)
        heapq.heappush(room,timeList[i][1])
        
print(len(room))