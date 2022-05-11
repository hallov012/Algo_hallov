import sys
sys.stdin = open('input.txt')

def multi(data_a, data_b):
    data = [[0] * n for _ in range(n)]
    for i in range(n):
        for a in range(n):
            value = 0
            for j in range(n):
                value += data_a[i][j] * data_b[j][a]
            data[i][a] = value % m
    return data

def square(data, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                data[i][j] %= m
        return data
    elif b % 2:
        return multi(square(data, b-1), data)
    else:
        return square(multi(data, data), b//2)

input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
m = 1000
ans = square(arr, b)
for line in ans:
    print(*line)


