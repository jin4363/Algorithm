import sys
from itertools import permutations
input = sys.stdin.readline

numstr = list(input().strip())
numstr.sort(reverse=True)
num = list(map(int,numstr))
sum = 0 
for x in num:
    sum += x
if sum % 3 != 0 or '0' not in numstr :
    print(-1)
else :
    print(''.join(numstr))
