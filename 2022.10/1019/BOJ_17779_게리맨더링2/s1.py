import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
total = 0
for line in data:
    total += sum(line)
ans = sys.maxsize
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if 0 <= x < n-d1-d2 and d1 <= y < n-d2:
                    cnt = [0] * 5
                    # 1번 구역
                    for i in range(x):
                        cnt[0] += sum(data[i][:y+1])
                    k = 0
                    for i in range(x, x+d1):
                        cnt[0] += sum(data[i][:y-k])
                        k += 1
                    # 2번 구역
                    for i in range(x):
                        cnt[1] += sum(data[i][y+1:])
                    k = 0
                    for i in range(x, x+d2+1):
                        cnt[1] += sum(data[i][y+k+1:])
                        k += 1
                    # 3번 구역
                    k = d1
                    for i in range(x+d1, x+d1+d2+1):
                        cnt[2] += sum(data[i][:y-k])
                        k -= 1
                    for i in range(x+d1+d2+1, n):
                        cnt[2] += sum(data[i][:y-d1+d2])
                    # 4번 구역
                    k = d2
                    for i in range(x+d2+1, x+d1+d2+1):
                        cnt[3] += sum(data[i][y+k:])
                        k -= 1
                    for i in range(x+d1+d2+1, n):
                        cnt[3] += sum(data[i][y-d1+d2:])
                    # 5번 구역
                    cnt[4] = total - sum(cnt)
                    ans = min(ans, max(cnt)-min(cnt))
print(ans)
