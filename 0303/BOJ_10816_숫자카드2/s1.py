import sys
sys.stdin = open('input.txt')

a = 10000000
n = int(input())
nums = list(map(int, input().split()))
cnt = [0] * (2 * a + 1)
for num in nums:
    cnt[num + a] += 1
m = int(input())
check = list(map(int, input().split()))
for num in check:
    print(cnt[num + a], end=' ')
