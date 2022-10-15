import sys, math
sys.stdin = open('input.txt')

a, b = map(int, input().split())
if b >= 10000000:
    b = 10000000
nums = [1] * (b+1)
nums[0] = nums[1] = 0
for i in range(2, int(math.sqrt(b+1))+1):
    if nums[i]:
        for j in range(i*2, b+1, i):
            nums[j] = 0
for i in range(a, b+1):
    if nums[i] and str(i) == str(i)[::-1]:
        print(i)
print(-1)