import sys
import itertools
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().strip().split()))
num.sort()
target=1
for x in num :
    if target < x :
        break
    target += x
print(target)