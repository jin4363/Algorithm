import sys
input = sys.stdin.readline

n = int(input())
scoreList = []
for _ in range(n):
    scoreList.append(int(input()))
ans =0
for i in range(n-2,-1,-1):
    if scoreList[i] >= scoreList[i+1] :
        while scoreList[i] != (scoreList[i+1] -1) :
            scoreList[i] -= 1
            ans +=1
print(ans)