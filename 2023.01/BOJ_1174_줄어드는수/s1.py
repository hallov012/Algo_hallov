import sys
sys.stdin = open('input.txt')

def dfs(last):
    if num:
        ans.append(int("".join(map(str, num))))
    for i in range(last-1, -1, -1):
        num.append(i)
        dfs(i)
        num.pop()


n = int(input())
ans = []
num = []
dfs(10)
ans.sort()
if n <= len(ans):
    print(ans[n-1])
else:
    print(-1)

