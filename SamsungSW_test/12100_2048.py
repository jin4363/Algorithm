import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
maps =[]
for _ in range(n):
    maps.append(list(map(int,input().split())))
