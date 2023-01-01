import sys, math
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
gab = []
ans = set()

for i in range(1, n):
    gab.append(nums[i] - nums[i-1])

prev = gab[0]
for i in range(1, len(gab)):
    prev = math.gcd(prev, gab[i])

for i in range(2, int(math.sqrt(prev))+1):
    if not prev % i:
        ans.add(i)
        ans.add(prev//i)
ans.add(prev)
ans = sorted(ans)
print(*ans)