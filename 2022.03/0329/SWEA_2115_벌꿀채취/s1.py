import sys
sys.stdin = open('input.txt')

def find(lst, cnt, gain, done):
    global sub_max
    if done == m:
        sub_max = max(sub_max, gain)
        return
    if cnt + lst[done] <= c:
        find(lst, cnt + lst[done], gain + lst[done] ** 2, done + 1)
    find(lst, cnt, gain, done + 1)

T = int(input())

for tc in range(1, T+1):
    n, m, c = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    gain_lst = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            sub = data[i][j: j+m]
            sub_max = 0
            find(sub, 0, 0, 0)
            gain_lst[i].append(sub_max)
    ans = 0
    for k in range(n):
        for l in range(len(gain_lst[k])):
            cnt = gain_lst[k][l]
            if l + m < len(gain_lst):
                for a in range(l+m, len(gain_lst[k])):
                    ans = max(ans, cnt + gain_lst[k][a])
            for x in range(k+1, n):
                for y in range(len(gain_lst[k])):
                    ans = max(ans, cnt + gain_lst[x][y])
    print(f'#{tc} {ans}')



