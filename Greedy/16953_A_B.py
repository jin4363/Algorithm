import sys
input = sys.stdin.readline
A,B = map(int,input().strip().split())
cnt =0 
while A < B :
    if B % 10 == 1 :
        B -= 1
        B /= 10
        cnt += 1
    else :
        if B % 2 == 0 :
            B /= 2
            cnt +=1
        else :
            break
if A == B :
    print(cnt+1)
else:
    print(-1)
