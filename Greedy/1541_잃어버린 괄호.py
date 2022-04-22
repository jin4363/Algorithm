# import sys
# input =sys.stdin.readline

# expr = input().strip().split('-')
# res = 0 
# # +만 있을경우 처리 
# for i in expr[0].split('+') :
#     res += int(i) 
# for i in expr[1:] :
#     for j in i.split('+'):
#         res -= int(j)
# print(res)

import sys
input =sys.stdin.readline

expr = input().strip().split('-')
res = 0 
# +만 있을경우 처리 
for i in expr[0].split('+') :
    res += int(i) 
for i in expr[1:] :
    res -= eval(i)
print(res)

