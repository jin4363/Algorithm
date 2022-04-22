import sys
input = sys.stdin.readline

n = int(input())
arrA = list(map(int,input().strip().split()))
arrB = list(map(int,input().strip().split()))

arrA.sort()
arrB.sort(reverse=True)
sum = 0
for i in range(n):
    sum += arrA[i] * arrB[i]
print(sum)