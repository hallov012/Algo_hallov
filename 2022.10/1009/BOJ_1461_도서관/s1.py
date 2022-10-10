import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
left = []
right = []
for num in data:
    if num < 0:
        left.append(num)
    else:
        right.append(num)

dist = []
left.sort()
right.sort(reverse=True)

for i in range(len(left)//m):
    dist.append(abs(left[i*m]))
if len(left)%m > 0:
    dist.append(abs(left[-(len(left)%m)]))

for i in range(len(right)//m):
    dist.append(right[i*m])
if len(right)%m > 0:
    dist.append(right[-(len(right)%m)])

dist.sort()
ans = dist.pop()
ans += 2 * sum(dist)
print(ans)

