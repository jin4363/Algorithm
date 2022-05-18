from math import factorial
from msilib import FCICreate
import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    ans = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
    print(ans)