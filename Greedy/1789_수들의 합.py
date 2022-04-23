import sys
input = sys.stdin.readline
s = int(input().strip())
x = 1 
while True :
    s -= x
    if s-x > 0 :
        x += 1
    else :
        break
print(x)