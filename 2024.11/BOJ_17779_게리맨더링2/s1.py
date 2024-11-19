import sys
sys.stdin = open('input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
total = 0
for row in data:
    for i in range(1, n):
        row[i] += row[i-1]

ans = sys.maxsize
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if 0 <= x < n-d1-d2 and d1 <= y < n-d2:
                    cnt = [0] * 5
                    for i in range(x):
                        cnt[0] += data[i][y]
                    k = 0
                    for i in range(x, x+d1):
                        
