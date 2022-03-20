import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    homes = []
    ans = 0
    for i in range(n):
        for j in range(n):
            if data[i][j]:
                homes.append([i, j])
    for i in range(n):
        for j in range(n):
            for k in range(1, 2*n):
                home_cnt = 0
                for home in homes:
                    if abs(home[0]-i) + abs(home[1]-j) < k:
                        home_cnt += 1
                if home_cnt != 0:
                    revenue = home_cnt * m
                    cost = k * k + (k - 1) * (k - 1)
                    if revenue >= cost:
                        ans = max(ans, home_cnt)
    print(f'#{tc} {ans}')


