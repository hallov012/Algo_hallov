import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
cnt = data[::]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            cnt[i] = max(cnt[i], cnt[j]+data[i])
print(max(cnt))