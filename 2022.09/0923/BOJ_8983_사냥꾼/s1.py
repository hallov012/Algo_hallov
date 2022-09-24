import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n, l = map(int, input().split())
spot = list(map(int, input().split()))
spot.sort()
animal = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for x, y in animal:
    start = 0
    end = m-1
    while start < end:
        mid = (start+end)//2
        if spot[mid] < x:
            start = mid+1
        else:
            end = mid
    if abs(spot[end]-x)+y <= l or abs(spot[end-1]-x)+y <= l:
        ans += 1
print(ans)