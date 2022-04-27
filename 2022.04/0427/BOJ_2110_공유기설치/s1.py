import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()
left = 1
right = homes[-1] - homes[0]
ans = 0
while left <= right:
    mid = (left + right) // 2
    now = homes[0]
    cnt = 1
    for i in range(1, n):
        if now + mid <= homes[i]:
            cnt += 1
            now = homes[i]
    if cnt >= c: # 거리를 더 늘려봐도 된다
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
print(ans)

