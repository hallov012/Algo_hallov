import sys
sys.stdin = open('input.txt')

def dfs(num, data):
    data[num] = -2
    for i in range(n):
        if num == data[i]:
            dfs(i, data)

n = int(input())
data = list(map(int, input().split()))
m = int(input())
dfs(m, data)
ans = 0
for i in range(n):
    if data[i] != -2 and i not in data:
        ans += 1
print(ans)