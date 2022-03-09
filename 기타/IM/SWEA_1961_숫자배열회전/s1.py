import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc}')
    for i in range(n):
        for a in range(n):
            print(data[n-a-1][i], end="")
        print('', end=" ")
        for b in range(n):
            print(data[n-i-1][n-b-1], end="")
        print('', end=" ")
        for c in range(n):
            print(data[c][n-i-1], end="")
        print()
