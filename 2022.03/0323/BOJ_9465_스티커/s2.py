import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    data = [[0] * n]
    for _ in range(2):
        data.append(list(map(int, input().split())))
    for i in range(1, n):
        data[0][i] += max(data[1][i-1], data[2][i-1])
        data[1][i] += max(data[0][i-1], data[2][i-1])
        data[2][i] += max(data[0][i-1], data[1][i-1])
    ans = 0
    for j in range(3):
        ans = max(ans, data[j][n-1])
    print(ans)

