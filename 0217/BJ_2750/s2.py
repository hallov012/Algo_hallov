import sys
sys.stdin = open('input.txt')

T = int(input())

data = []
for _ in range(T):
    num = int(sys.stdin.readline())
    data.append(num)

max_n = max(data)

cnt = [0] * (max_n + 1)
ans = [0] * T
for i in data:
    cnt[i] += 1

for i in range(max_n):
    cnt[i+1] += cnt[i]

for i in data:
    ans[cnt[i]-1] = i
    cnt[i] -= 1

for i in range(T):
    print(ans[i])


# 왜 오답이야...?