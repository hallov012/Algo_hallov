import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    temp = data[-1]
    for i in range(n-1, -1, -1):
        if data[i] < temp:
            cnt += temp - data[i]
        else:
            temp = data[i]
    print(cnt)
