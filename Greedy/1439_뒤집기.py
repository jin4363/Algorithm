import sys
input = sys.stdin.readline

s = input()
optS = ''
now='?'
oneCnt = 0
zeroCnt = 0
for i in s :
    if now != i :
        now = i 
        optS += i
        if i == '1':
            oneCnt += 1
        elif i == '0':
            zeroCnt += 1
            
if oneCnt >=1 and zeroCnt >= 1 :
    print(min(oneCnt,zeroCnt))
else :
    print(0)
        