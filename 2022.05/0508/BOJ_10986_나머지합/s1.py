import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
cnt = [[0] * (n+1) for _ in range(n+1)]
ans = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        cnt[j][i] += nums[i-1]
        if not cnt[j][i] % m:
            ans += 1
print(ans)