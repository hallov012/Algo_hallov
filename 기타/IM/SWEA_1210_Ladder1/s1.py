import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    data = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    r = 99
    c = data[r].index(2)
    while r > 0:
        if data[r][c-1]:
            while data[r][c-1]:
                c -= 1
        elif data[r][c+1]:
            while data[r][c+1]:
                c += 1
        r -= 1
    print(f'#{tc} {c-1}')
