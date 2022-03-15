import sys
sys.stdin = open('input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
time = [0] * (2 ** 13)
meetings = sorted(data, key=lambda x: (x[1], x[0]))
ans = 0
end_time = 0
for time in meetings:
    s, e = time
    if s >= end_time:
        ans += 1
        end_time = e
print(ans)
