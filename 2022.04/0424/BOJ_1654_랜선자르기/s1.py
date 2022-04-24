import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

k, n = map(int, input().split())
lans = list(int(input()) for _ in range(k))
left, right = 1, max(lans)

while left <= right:
    mid = (left + right) // 2
    lan_cnt = 0
    for lan in lans:
        lan_cnt += lan // mid
    if lan_cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)