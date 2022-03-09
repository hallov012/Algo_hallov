import sys
sys.stdin = open('input.txt')

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * 101 for _ in range(101)]
cnt = 0
for i in range(n):
    for a in range(data[i][0], data[i][0]+10):
        for b in range(data[i][1], data[i][1]+10):
            if not arr[a][b]:
                arr[a][b] += 1
                cnt += 1
print(cnt)