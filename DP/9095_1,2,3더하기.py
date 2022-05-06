import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
t = int(input())

def solve(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else :
        return solve(x-1) + solve(x-2) + solve(x-3)

for _ in range(t):
    n = int(input())
    print(solve(n))