import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
gab = []
for i in range(1, n):
    gab.append(data[i] - data[i-1])
gab.sort()
print(sum(gab[:n-k]))