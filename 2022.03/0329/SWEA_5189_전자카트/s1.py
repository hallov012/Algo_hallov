import sys
sys.stdin = open('input.txt')

def min_sum(start, done, cnt):
    global ans
    if cnt > ans:
        return
    if done == n-1:
        cnt += data[start][0]
        ans = min(ans, cnt)
        return
    else:
        for i in range(1, n):
            if i != start:
                if not visited[i]:
                    visited[i] = 1
                    min_sum(i, done+1, cnt + data[start][i])
                    visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    visited[0] = 1
    ans = 100 * (n ** 2)
    min_sum(0, 0, 0)
    print(f'#{tc} {ans}')