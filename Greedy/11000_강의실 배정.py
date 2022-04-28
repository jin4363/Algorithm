import sys
input = sys.stdin.readline

n = int(input().strip())
timeList = []
for _ in range(n):
    timeList.append(list(map(int,input().split())))
    
timeList.sort(key=lambda x : x[0])
cnt = 0
using = set()
for i in timeList :
    if not using :
        for num in range(i[0],i[1]+1):
            using.add(num)
    else :
        if i[0] in using :
            cnt +=1
        else :
            for num in range(i[0],i[1]+1):
                using.add(num)
print(cnt)