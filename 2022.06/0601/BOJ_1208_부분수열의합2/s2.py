import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(sum, idx, end, sum_set):
    global ans
    for i in range(idx, end):
        if not visited[i]:
            sum += nums[i]
            visited[i] = 1
            if sum == s:
                ans += 1
            sum_set[sum] += 1
            dfs(sum, i+1, end, sum_set)
            sum -= nums[i]
            visited[i] = 0

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * (n+1)
mid = n // 2
ans = 0
left_sum = defaultdict(int)
right_sum = defaultdict(int)

dfs(0, 0, mid, left_sum)
dfs(0, mid, n, right_sum)

left_num = list(left_sum.keys())
right_num = list(right_sum.keys())

left_num.sort()
right_num.sort()

left, right = 0, len(right_num) - 1
while left < len(left_num) and right >= 0:
    check = left_num[left] + right_num[right]
    if check == s:
        ans += left_sum[left_num[left]] * right_sum[right_num[right]]
        left += 1
        right -= 1
    elif check > s:
        right -= 1
    else:
        left += 1

print(ans)


