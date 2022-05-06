import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    nums[i] += nums[i-1]
for _ in range(m):
    a, b = map(int, input().split())
    ans = nums[b] - nums[a-1]
    print(ans)