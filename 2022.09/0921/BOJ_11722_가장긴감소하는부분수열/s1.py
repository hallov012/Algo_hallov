import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
ans = [1] * n
data = list(reversed(data))

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            ans[i] = max(ans[i], ans[j] + 1)
print(max(ans))