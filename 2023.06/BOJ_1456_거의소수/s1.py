import math
import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
n = int(math.sqrt(b))
nums = [1] * (n+1)
nums[0] = nums[1] = 0
for i in range(2, n+1):
    if i * i > n:
        break
    if nums[i]:
        for j in range(i*i, n+1, i):
            nums[j] = 0

ans = 0
for i in range(1, n+1):
    if nums[i]:
        j = i * i
        while True:
            if j < a:
                j *= i
                continue
            if j > b:
                break
            j *= i
            ans += 1

print(ans)