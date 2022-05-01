import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cnt = 0
if n == 1 :
    cnt = 1
elif n == 2 :
    res = ((m-1)//2) +1
    cnt = min(res,4)
elif m<7 :
    cnt = min(m,4)
else:
    cnt = (2 + (m-5)) +1
print(cnt)