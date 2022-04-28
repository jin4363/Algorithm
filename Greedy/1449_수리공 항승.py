import sys
input=sys.stdin.readline

N,L = map(int,input().split())
targetList = list(map(int,input().split()))
fixList = [0 for _ in range(N)]
targetList.sort()
cnt=0
idx=0  
while idx < N :
    flag = 0
    start = targetList[idx] - 0.5
    end = start + L
    cnt += 1
    tempIdx = idx
    for j in targetList[idx:] :
        if float(start) < float(j) < float(end) :
            fixList[tempIdx] = 1
            tempIdx+=1
            flag=1
        else :
            break
    if flag == 1:
        idx = tempIdx
    else :
        idx +=1
           
print(cnt)