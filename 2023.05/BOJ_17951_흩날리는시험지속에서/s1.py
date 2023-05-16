import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
left, right = 0, int(1e5)*20+1
while left <= right:
    mid = (left+right)//2
    cnt, temp = 0, 0
    for num in data:
        temp += num
        if temp >= mid:
            cnt += 1
            temp = 0
    if cnt >= k:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)