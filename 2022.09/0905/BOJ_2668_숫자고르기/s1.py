import sys
sys.stdin = open('input.txt')

def dfs(row1, row2, num):
    row1.add(num)
    row2.add(data[num])
    if data[num] in row1:
        if row1 == row2:
            ans.update(row1)
            return True
        return False
    dfs(row1, row2, data[num])

input = sys.stdin.readline

n = int(input())
data = [0] + [int(input()) for _ in range(n)]
ans = set()

for i in range(1, n+1):
    if i not in ans:
        dfs(set(), set(), i)

print(len(ans))
ans = sorted(list(ans))
for num in ans:
    print(num)


