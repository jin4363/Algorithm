import sys
input = sys.stdin.readline

#이분 탐색O(NlogN)
def bisect_left(arr,val):
    s,e = 0,len(arr)-1
    while s <= e :
        #//는 몫 연산자
        mid = (s+e)//2
        if arr[mid] > val :
            e = mid - 1 
        else :
            s = mid + 1
    return s

n = int(input())
ports = list(map(int,input().strip().split()))
LISList=[]
for x in ports:
    if not LISList or LISList[-1] < x:
        LISList.append(x)
    else :
        #from bisect import bisect_left 모듈 가져오면 함수 사용도 가능 
        LISList[bisect_left(LISList,x)] = x
print(len(LISList))