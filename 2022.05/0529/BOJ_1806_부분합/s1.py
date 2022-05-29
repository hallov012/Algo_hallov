import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
sum = 0
ans = 10 ** 5
while True:
    if sum >= s:
        ans = min(ans, right - left)
        sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        sum += nums[right]
        right += 1

if ans == 10 ** 5:
    print(0)
else:
    print(ans)

