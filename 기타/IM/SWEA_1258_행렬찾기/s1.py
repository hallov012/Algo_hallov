import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            a, b = 0, 0
            if not data[i][j]:
                continue
            else:
                while data[i+a][j] != 0 and i + a < n:
                    a += 1
                while data[i][j+b] != 0 and j + b < n:
                    b += 1
                ans.append([a, b])
            for r in range(a+1):
                for c in range(b+1):
                    data[i+r][j+c] = 0
    for i in range(len(ans)-1, 0 , -1):
        for j in range(i):
            if ans[i][0] * ans[i][1] < ans[j][0] * ans[j][1]:
                ans[i], ans[j] = ans[j], ans[i]
    print(f'#{tc} {len(ans)}', end=" ")
    for i in ans:
        print(*i, end=" ")
    print()
