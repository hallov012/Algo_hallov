import sys
sys.stdin = open('input.txt')

n = int(input())
m = 10 ** 9
nums = list(map(int, input().split()))
cnt = [0] * (2 * m+ 1)
ans = [0] * n
for num in nums:
    cnt[num + m] += 1
for num in nums:
    for i in range(num + m):
        if cnt[i] > 0:
            ans[i] += 1
print(*ans)