import sys
input = sys.stdin.readline

docStr = input().strip()
searchStr = input().strip()
idx = 0
flag=0
cnt=0
while idx < (len(docStr) - len(searchStr) + 1) and searchStr in docStr:
    if str(searchStr) == str(docStr[idx:idx + (len(searchStr))]) :
        cnt += 1
        idx += (len(searchStr))
    else :
        idx += 1
print(cnt)
    