import sys
sys.stdin = open('input.txt')

n = int(input())
times = list(map(int, input().split()))
times.sort()
ans = 0
cnt = [0] * n
for i in range(n):
    if not i:
        cnt[i] = times[i]
    else:
        cnt[i] = times[i] + cnt[i-1]
print(sum(cnt))