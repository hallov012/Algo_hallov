import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            ans[i] = max(ans[i], ans[j]+1)
print(max(ans))


