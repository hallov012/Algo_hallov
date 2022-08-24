import sys
sys.stdin = open('input.txt')

n = int(input())
k = int(input())
data = list(map(int, input().split()))
data.sort()
ans = 0
if k >= n:
    print(0)
    exit()
dist = []
for i in range(1, n):
    dist.append(data[i]-data[i-1])
dist.sort()
print(sum(dist[:n-k]))


