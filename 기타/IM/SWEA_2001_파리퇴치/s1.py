import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]
    max_die = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly_cnt = 0
            for a in range(m):
                for b in range(m):
                    fly_cnt += fly[i+a][j+b]
            if max_die < fly_cnt:
                max_die = fly_cnt
    print(f'#{tc} {max_die}')
