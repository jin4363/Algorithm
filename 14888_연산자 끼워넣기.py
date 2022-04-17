import sys
input = sys.stdin.readline

numberCount = int(input())
numberArray = list(map(int,input().split()))
plusCount, subCount, mulCount, divCount = map(int, input().split())

maxSum = -1000000000
minSum = 1000000000

def dfs(depth, total, plus, minus, multi, divide):
    global maxSum, minSum
    if depth == numberCount:
        maxSum = max(total,maxSum)
        minSum = min(total,minSum)
        return
    if plus>0 :
        dfs(depth+1,total+numberArray[depth],plus-1,minus,multi,divide)
    if minus>0:
        dfs(depth+1,total-numberArray[depth],plus,minus-1,multi,divide)
    if multi>0 :
        dfs(depth+1,total*numberArray[depth],plus,minus,multi-1,divide)
    if divide>0:
        dfs(depth+1,int(total/numberArray[depth]),plus,minus,multi,divide-1)

dfs(1,numberArray[0],plusCount,subCount,mulCount,divCount)



print(maxSum)
print(minSum)
