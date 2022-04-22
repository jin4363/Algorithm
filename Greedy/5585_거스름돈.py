import sys
input =sys.stdin.readline

num = int(input())
ans =0
num = 1000 - num
if num >= 500 :
    cnt = int(num / 500)
    num -=500*cnt
    ans += cnt
if num >= 100 :
    cnt = int(num / 100)
    num -=100*cnt
    ans += cnt
if num >= 50 :
    cnt = int(num / 50)
    num -=50*cnt
    ans += cnt
if num >= 10 :
    cnt = int(num / 10)
    num -=10*cnt
    ans += cnt
if num >= 5 :
    cnt = int(num / 5)
    num -=5*cnt
    ans += cnt
if num >= 1 :
    cnt = int(num / 1)
    num -=1*cnt
    ans += cnt
print(ans)

    
