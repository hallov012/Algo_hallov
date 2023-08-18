import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = []
for num in nums:
    binary = bin(num)[2:]
    cnt.append((binary.count('1'), num))

cnt.sort(reverse=True)
print(cnt[k-1][1])