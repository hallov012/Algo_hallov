import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            x, y, z = data[a], data[b], data[c]
            d1 = (x[0]-y[0])**2 + (x[1]-y[1])**2
            d2 = (x[0]-z[0])**2 + (x[1]-z[1])**2
            d3 = (y[0]-z[0])**2 + (y[1]-z[1])**2
            if max(d1, d2, d3) * 2 == d1 + d2 + d3:
                ans += 1
print(ans)